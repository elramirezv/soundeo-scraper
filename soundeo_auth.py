import pickle
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    with open("soundeo_cookies.pkl", "rb") as file:
        cookies = pickle.load(file)
        for cookie in cookies:
            driver.add_cookie(cookie)
    
    return driver
