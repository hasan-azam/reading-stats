from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os
from dotenv import load_dotenv

#Pulling login credentials from .env file
load_dotenv()

STORYGRAPH_EMAIL = os.getenv("STORYGRAPH_EMAIL")
STORYGRAPH_PASSWORD = os.getenv("STORYGRAPH_PASSWORD")

#Checks to make sure the credentials got loaded

if not STORYGRAPH_EMAIL or not STORYGRAPH_PASSWORD:
    raise ValueError("Email or password not set in .env file!")


#Setting up the Chrome options for custom download directory

relative_path = "data/raw-data/books/"
download_dir = os.path.abspath(relative_path)
print("Download directory set to:", download_dir)


chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False, #Disables download prompts
    "download.directory_upgrade": True, #Overwrites whatever's in there already
    "safebrowsing.enabled": True,
})

#chrome_options.add_argument("--headless=new")  # Run Chrome in headless mode
chrome_options.add_argument("--disable-gpu")  # Disable GPU usage (optional)
chrome_options.add_argument("--no-sandbox")   # Useful for certain Linux environments
chrome_options.add_argument("--disable-dev-shm-usage")  # Improve performance in some systems

#initializes webdriver with those options

driver = webdriver.Chrome(options=chrome_options) #uses Chrome as the web driver


try:
    #Open up the login page
    driver.get("https://app.thestorygraph.com/users/sign_in")

    #Wait for Login page to load

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "user[email]"))
    )

    #find the email input field and send it my email
    #make this more secure
    email_input = driver.find_element(By.NAME, "user[email]")
    email_input.send_keys(STORYGRAPH_EMAIL)

    #find password field and fill it
    #make this more secure

    password_input = driver.find_element(By.NAME, "user[password]")
    password_input.send_keys(STORYGRAPH_PASSWORD)
    password_input.send_keys(Keys.RETURN)

    #Wait for Dashboard to Load

    WebDriverWait(driver, 10).until(
        EC.url_matches("https://app.thestorygraph.com/")
    )

    #Takes us to user export page
    driver.get("https://app.thestorygraph.com/user-export")


    #Wait for Export Button and clicks it, then waits for generation
    export_button = WebDriverWait(driver, 10).until(
         EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Generate export')]"))
    )

    export_button.click()

    time.sleep(15)

    #Refreshes page and clicks download button

    driver.refresh()

    download_button = WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Download"))
    )

    download_button.click()

    time.sleep(2)
    print("Storygraph download completed successfully!")
finally:
    driver.quit()