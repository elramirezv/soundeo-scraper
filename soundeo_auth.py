import os
import pickle
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from driver_setup import driver


def login(driver):
    account_link = driver.find_element(By.CSS_SELECTOR, "a[href='/account/logoreg']")
    account_link.click()

    wait = WebDriverWait(driver, 10)
    username_input = wait.until(EC.presence_of_element_located((By.ID, "UserLogin")))
    password_input = driver.find_element(By.ID, "UserPassword")

    username_input.send_keys("raulsalazar@uc.cl")
    password_input.send_keys("Soundeo12345")

    login_button = driver.find_element(By.CSS_SELECTOR, "button.signin-btn")

    login_button.click()


def download_cookies(driver):
    cookies = driver.get_cookies()
    with open("soundeo_cookies.pkl", 'wb') as file:
        pickle.dump(cookies, file)

def set_cookies(driver):
    if not os.path.exists("soundeo_cookies.pkl"):
        raise Exception("No cookies found: You must login first running 'python soundeo_auth.py'")
    
    with open("soundeo_cookies.pkl", "rb") as file:
        cookies = pickle.load(file)
        for cookie in cookies:
            driver.add_cookie(cookie)
    
    return driver

if __name__ == "__main__":
    print("Going to login page")
    login(driver)
    print("Logged in")
    time.sleep(3)
    download_cookies(driver)
    driver.quit()