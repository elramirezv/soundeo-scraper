import os


def check_if_file_exists(file_path):
    return os.path.exists(file_path)


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