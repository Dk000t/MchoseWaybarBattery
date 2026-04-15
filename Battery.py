import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Wait for a connection to be present so as not to fail to upload the battery status to waybar
def wait_connection():
    while True:
        try:
            response = requests.get("https://www.google.com", timeout=3)    
            
            if response.status_code == 200:
                return
                
        except requests.RequestException:
            pass
            
        time.sleep(2)

# URL of the target page to automate
URL = "https://www.mchose.com.cn/#/detail?deviceName=MCHOSE+A7+V2+Ultra"

# Get the path to the current user's home directory
HOME = os.path.expanduser("~")

# Path to the Chromium/Chrome user data directory
CHROME_PROFILE_PATH = f"{HOME}/.config/chromium_battery"

# Initialize Chrome options object
options = Options()

# Set the path to the Chrome user data directory, so Chrome uses this profile's data (cookies, bookmarks, extensions, etc.)
options.add_argument(f"user-data-dir={CHROME_PROFILE_PATH}")

# Launch chromium in headless mode
options.add_argument("--headless=new")

# Disable sandbox
options.add_argument("--no-sandbox")

# Disable gpu
options.add_argument("--disable-gpu")

try:
    wait_connection()
    
    # Creates a chromium instance with the defined options
    driver = webdriver.Chrome(options=options)
    
    # Open the defined URL
    driver.get(URL)
    
    # Wait until all values ​​have been updated, this prevents placeholders from being used before the battery status is queried.
    time.sleep(2)
    
    # Get the mouse name
    name = driver.find_element(By.CSS_SELECTOR, ".name")
    
    # Get battery percentage
    battery = driver.find_element(By.CSS_SELECTOR, ".other-equipment")
    
    # Print the battery icon, name and percentage
    print("" + "  " + battery.text + " " + "-" + " " + "MCHOSE" + " " + name.text)

finally:
    # Close chromium
    driver.quit()
