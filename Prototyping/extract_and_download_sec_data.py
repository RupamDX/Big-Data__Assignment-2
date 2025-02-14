#working

import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Configuration
SEC_URL = "https://www.sec.gov/dera/data/financial-statement-data-sets.html"
DOWNLOAD_FOLDER = "D:/NEU/SEM2/BigData/ASSIGNMENT2/sec_datasets"
CONTACT_EMAIL = "your.email@example.com"  # Use your actual email
SEC_USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36 (Contact: {})".format(CONTACT_EMAIL)
)

# Ensure the download folder exists
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

# Set up Selenium Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run headless
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("disable-infobars")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument(f"user-agent={SEC_USER_AGENT}")

def get_sec_dataset_links_and_cookies():
    """Scrape SEC dataset links (ZIP files) using Selenium and return the links along with cookies."""
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    try:
        driver.get(SEC_URL)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "a")))
        links = [
            elem.get_attribute("href")
            for elem in driver.find_elements(By.TAG_NAME, "a")
            if elem.get_attribute("href") and elem.get_attribute("href").endswith(".zip")
        ]
        # Extract cookies from the Selenium session
        cookies = driver.get_cookies()
        return links, cookies
    except Exception as e:
        print(f"Error fetching SEC data: {e}")
        return [], []
    finally:
        driver.quit()

def download_file(url, folder, cookies):
    """Download a file from a URL into the specified folder, using provided cookies and headers."""
    filename = os.path.join(folder, url.split("/")[-1])
    headers = {
        "User-Agent": SEC_USER_AGENT,
        "From": CONTACT_EMAIL,
        "Referer": "https://www.sec.gov/",
        "Accept": "application/zip, application/octet-stream, application/x-zip-compressed, multipart/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.5",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive"
    }
    try:
        session = requests.Session()
        # Add cookies from Selenium to the requests session
        for cookie in cookies:
            session.cookies.set(cookie['name'], cookie['value'])
        response = session.get(url, headers=headers, stream=True)
        response.raise_for_status()  # Raise exception for HTTP errors
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        print(f"Downloaded: {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")

if __name__ == "__main__":
    dataset_links, cookies = get_sec_dataset_links_and_cookies()
    if not dataset_links:
        print("No dataset links found.")
    for link in dataset_links:
        time.sleep(2)  # Pause between downloads to mimic human behavior
        download_file(link, DOWNLOAD_FOLDER, cookies)
