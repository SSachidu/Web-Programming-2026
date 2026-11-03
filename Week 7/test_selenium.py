from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = "/usr/bin/google-chrome"
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")

browser = webdriver.Chrome(options=options)

browser.get("https://example.com")
assert browser.page_source.find('Example Domain') != -1, "ERROR - page not found"

print("Selenium working as expected")

browser.quit()