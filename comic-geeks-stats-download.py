from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os


#Setting up the Chrome options for custom download directory

relative_path = "data/raw-data/comics/"
download_dir = os.path.abspath(relative_path)
print("Download directory set to:", download_dir)


chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False, #Disables download prompts
    "download.directory_upgrade": True, #Overwrites whatever's in there already
    "safebrowsing.enabled": True,
})

chrome_options.add_argument("--headless=new")  # Run Chrome in headless mode
chrome_options.add_argument("--disable-gpu")  # Disable GPU usage (optional)
chrome_options.add_argument("--no-sandbox")   # Useful for certain Linux environments
chrome_options.add_argument("--disable-dev-shm-usage")  # Improve performance in some systems

#initializes webdriver with those options

driver = webdriver.Chrome(options=chrome_options) #uses Chrome as the web driver

comic_geeks_username="hasan"

try:
    #Open up the login page
    driver.get("https://leagueofcomicgeeks.com/login")

    #Wait for Login page to load

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )

    #find the username input field and send it my username
    #make this more secure
    username_input = driver.find_element(By.NAME, "username")
    username_input.send_keys(comic_geeks_username)

    #find password field and fill it
    #make this more secure

    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys("_YmKa#r85.xM7DM")
    password_input.send_keys(Keys.RETURN)


 #Wait for Dashboard to Load

    WebDriverWait(driver, 10).until(
        EC.url_matches("https://leagueofcomicgeeks.com/dashboard")
    )

#take us to download page
    driver.get(f"https://leagueofcomicgeeks.com/profile/{comic_geeks_username}/import-comics")

 #Wait for Export Button and clicks it, then waits for generation
    export_button = WebDriverWait(driver, 10).until(
         EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Export My Comics')]"))
    )

    export_button.click()
    time.sleep(4)


    

finally:
    driver.quit()