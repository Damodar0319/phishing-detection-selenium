from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def setup_driver():
    options = Options()
    options.add_argument("--headless=new")  # better for latest Chrome
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--single-process")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    return driver