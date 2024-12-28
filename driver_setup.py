from selenium import webdriver


download_dir = "/Users/alekhan/Downloads/Musica"

chrome_options = webdriver.ChromeOptions()
preferences = {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "profile.default_content_settings.popups": 0,  # Deshabilitar ventanas emergentes
    "safebrowsing.enabled": True
}
chrome_options.add_experimental_option("prefs", preferences)
chrome_options.set_capability("pageLoadStrategy", "normal")

driver = webdriver.Chrome(options=chrome_options)



