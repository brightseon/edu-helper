from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
import os
import time

load_dotenv()

URL = os.environ.get('url')
ID = os.environ.get('id')
PASSWORD = os.environ.get('password')
LISTEN_COURSED_IDX = os.environ.get('listen_coursed_idx')


def main():
    try:
        driver = webdriver.Chrome(service=Service(
            ChromeDriverManager().install()))
        driver.get(URL)

        for win in driver.window_handles[1:]:
            time.sleep(0.4)
            driver.switch_to.window(win)
            driver.close()

        driver.switch_to.window(driver.window_handles[0])

        time.sleep(0.3)
        id_box = driver.find_element(by=By.ID, value='userInputId')
        password_box = driver.find_element(by=By.ID, value='userInputPw')
        login_button = driver.find_element(
            by=By.CSS_SELECTOR, value='a.btn_basic_color.btn_basic.one')

        for s in ID:
            time.sleep(0.4)
            id_box.send_keys(s)

        time.sleep(0.3)

        for s in PASSWORD:
            time.sleep(0.4)
            password_box.send_keys(s)

        time.sleep(0.3)
        login_button.click()

        time.sleep(2)
        for win in driver.window_handles[1:]:
            time.sleep(2)
            driver.switch_to.window(win)
            driver.close()

        driver.switch_to.window(driver.window_handles[0])

        time.sleep(2)
        courses_taking = driver.find_element(
            by=By.CSS_SELECTOR, value='a[title="수강중인과정 바로가기"]')

        courses_taking.click()

        time.sleep(2)
        driver.switch_to.window(driver.window_handles[-1])

        time.sleep(2)
        listen_courses = driver.find_elements(
            by=By.CSS_SELECTOR, value='a.bnt_basic_line.small')
        listen_courses[int(LISTEN_COURSED_IDX)].click()

        time.sleep(2)
        driver.switch_to.window(driver.window_handles[-1])

        time.sleep(2)

        display_course_complete = False
        while display_course_complete == False:
            time.sleep(2)
            next_button = driver.find_element(
                by=By.CSS_SELECTOR, value='button.next-btn.vjs-control')

            if driver.find_element(by=By.CSS_SELECTOR, value='iframe.quizPage').value_of_css_property('display') != 'none':
                next_button.click()

            time.sleep(5)
            play_button = driver.find_element(
                by=By.CSS_SELECTOR, value='button.vjs-big-play-button')

            if play_button.value_of_css_property('display') != 'none':
                play_button.click()

            time.sleep(5)
            action = ActionChains(driver)
            action.move_to_element(driver.find_element(
                by=By.CSS_SELECTOR, value='div#lx-player')).perform()

            video_duration = driver.find_element(
                by=By.CSS_SELECTOR, value='span.vjs-duration-display')
            if video_duration.text != '':
                split_video_duration = video_duration.text.split(':')
                secs = int(split_video_duration[0]) * \
                    60 + int(split_video_duration[1]) + 10
                time.sleep(secs)
            else:
                time.sleep(10)

            if driver.find_element(by=By.CSS_SELECTOR, value='span.click_tooltip').value_of_css_property('display') != 'none':
                next_button.click()

            time.sleep(3)
            display_course_complete = driver.find_element(
                by=By.XPATH, value='//*[contains(text(), "마지막 목차입니다.")]').is_displayed()

        time.sleep(3)

        driver.quit()
    except Exception as e:
        print(e)
    finally:
        driver.quit()


if __name__ == '__main__':
    main()
