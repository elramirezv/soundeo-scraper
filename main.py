import time
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from soundeo_auth import login, download_cookies, set_cookies
from config import DOWNLOAD_DIR
from driver_setup import driver

driver.get("https://soundeo.com")
driver.delete_all_cookies()
# time.sleep(3)
driver = set_cookies(driver)
print("Going to page https://soundeo.com/account/downloads")
driver.get("https://soundeo.com/account/downloads")
time.sleep(3)


# print("Going to login page")
# login(driver)
# print("Logged in")
# time.sleep(3)
# download_cookies(driver)
# driver.quit()

wait = WebDriverWait(driver, 10)
wait.until(EC.url_contains("account/downloads"))


def song_exists(song_title):
    # Clean the song title to match file naming
    clean_title = song_title.replace('/', '_').replace('\\', '_')
    # Check for both .aiff and .mp3 extensions
    possible_files = [
        os.path.join(DOWNLOAD_DIR, f"{clean_title}.aiff"),
        os.path.join(DOWNLOAD_DIR, f"{clean_title}.mp3")
    ]
    return any(os.path.exists(file) for file in possible_files)

def download_aiff_files(driver):
    songs = driver.find_elements(By.CLASS_NAME, "trackitem")
    for song_element in songs:
        song_title = song_element.find_element(By.CSS_SELECTOR, "div.info strong a").text
        if song_exists(song_title):
            print(f"Skipping {song_title} - already downloaded")
            continue
            
        aiff_link = song_element.find_element(By.CSS_SELECTOR, ".track-download-lnk[data-track-format='1']")
        print(f"Downloading {song_title}")
        aiff_link.click()
        time.sleep(3)

def get_last_page_number(wait):
    pagination_element = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.pagination ul"))
    )
    links = pagination_element.find_elements(By.TAG_NAME, "a")
    last_page_link = links[-1]
    return int(last_page_link.get_attribute("href").split("=")[-1])


def go_to_page(driver, page_number):
    page_url = f"https://soundeo.com/account/downloads?page={page_number}"
    print(f"Going to page {page_url}")
    driver.get(page_url)
    time.sleep(1)


last_page_number = get_last_page_number(wait)
print("LAST PAGE NUMBER", last_page_number)

download_aiff_files(driver)

for page_number in range(2, last_page_number + 1):
    go_to_page(driver, page_number)
    download_aiff_files(driver)

driver.quit()
