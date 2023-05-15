from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
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
        play_button = driver.find_element(by=By.CSS_SELECTOR,
                                          value='button.vjs-big-play-button')
        play_button.click()

        time.sleep(3)

        driver.quit()
    except Exception as e:
        print(e)
        driver.quit()


if __name__ == '__main__':
    main()
