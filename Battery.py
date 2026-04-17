import os
import time
import requests
import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import SessionNotCreatedException

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

# Kill chromedriver and chromium processes
def kill_zombie_processes():
    subprocess.run(
        ["killall", "chromedriver", "chromium"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL    
    )

#Selenium can only start one session per user dir, when you reload the Sway configuration with ctrl+shift+c waybar restarts the script leaving chromedriver and chromium as zombie processes without being able to return the battery status, the same thing would happen if at the temporal activation of the script defined by the module settings in the waybar configuration and the Sway configuration is reloaded, so, if the driver has already been created, kill the processes and create the driver again.
def create_driver(retries = 1):
    for attempt in range(retries + 1):
        try:
            driver = webdriver.Chrome(options=options)
            return driver
        
        except SessionNotCreatedException:
            if attempt >= retries:
                raise
            
        kill_zombie_processes()

# URL of the target page to automate
URL = "https://www.mchose.com.cn/#/detail?deviceName=MCHOSE+A7+V2+Ultra"

# Get the path to the current user's home directory
HOME = os.path.expanduser("~")

# Path to the chromium user data directory
CHROMIUM_PROFILE_PATH = f"{HOME}/.config/chromium_battery"

# Initialize chromium options object
options = Options()

# Set the path to the chromium user data directory, so chromium uses this profile's data (cookies, bookmarks, extensions, etc.)
options.add_argument(f"user-data-dir={CHROMIUM_PROFILE_PATH}")

# Set up chromium options
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")

# Create chromium driver
driver = create_driver()

# Timeout
wait = WebDriverWait(driver, 10)  

# Wait for a connection to be available
wait_connection()

# Open the URL
driver.get(URL)
    
# Grab mouse name 
name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".name"))) 

# Grab battery status 
battery = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".other-equipment")))

# Avoid placeholder values ​​in the battery, waiting until an item is visible is not enough.
time.sleep(2)
    
# Print the battery icon, name and percentage
print("" + "  " + battery.text + " " + "-" + " " + "MCHOSE" + " " + name.text)

# Close chromium
driver.quit()
