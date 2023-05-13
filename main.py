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


def main():
    try:
        driver = webdriver.Chrome(service=Service(
            ChromeDriverManager().install()))
        driver.get(URL)

        for win in driver.window_handles[1:]:
            driver.switch_to.window(win)
            driver.close()

        driver.switch_to.window(driver.window_handles[0])

        id_box = driver.find_element(by=By.ID, value='userInputId')
        password_box = driver.find_element(by=By.ID, value='userInputPw')
        id_box.send_keys(ID)
        password_box.send_keys(PASSWORD)

        time.sleep(3)

        driver.quit()
    except Exception as e:
        print(e)
        driver.quit()


if __name__ == '__main__':
    main()
