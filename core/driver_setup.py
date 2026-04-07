from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def setup_driver():
    options = Options()
    options.page_load_strategy = 'eager'  # 🚀 Don't wait for heavy ads/trackers
    
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-extensions")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-notifications")
    
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(20)  # 🚀 Hard limit to stop waiting on infinite loading pages
    driver.maximize_window()

    return driver