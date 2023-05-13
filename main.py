from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
import os
import time

load_dotenv()

URL = os.environ.get('url')


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(URL)

    for win in driver.window_handles[1:]:
        driver.switch_to.window(win)
        driver.close()

    time.sleep(3)

    driver.quit()


if __name__ == '__main__':
    main()
