import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from driver_setup import driver
from soundeo_auth import download_cookies, login, set_cookies
from utils import download_aiff_files, get_last_page_number, go_to_page

if __name__ == "__main__":
    
    driver.get("https://soundeo.com")
    driver.delete_all_cookies()
    time.sleep(3)

    driver = set_cookies(driver)
    print("Going to page https://soundeo.com/account/downloads")
    driver.get("https://soundeo.com/account/downloads")
    time.sleep(3)

    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains("account/downloads"))

    last_page_number = get_last_page_number(wait)
    print("LAST PAGE NUMBER", last_page_number)
    download_aiff_files(driver)
    for page_number in range(2, last_page_number + 1):
        go_to_page(driver, page_number)
        download_aiff_files(driver)

    driver.quit()