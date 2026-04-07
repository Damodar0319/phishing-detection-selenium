from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def setup_driver():
    options = Options()
    options.add_argument("--headless=new")  # better for latest Chrome
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    return driver