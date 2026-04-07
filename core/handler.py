from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class UniversalWebHandler:
    def __init__(self, driver, timeout=10, retry=3):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.retry = retry

    def open_url(self, url):
        try:
            self.driver.get(url)
            return True
        except Exception as e:
            print(f"[ERROR] Could not open {url} -> {e}")
            return False

    def safe_find(self, locator):
        for _ in range(self.retry):
            try:
                return self.wait.until(EC.presence_of_element_located(locator))
            except:
                time.sleep(1)
        return None

    def safe_find_all(self, locator):   # ✅ added (useful for detectors)
        try:
            return self.driver.find_elements(*locator)
        except:
            return []

    def get_page_source(self):
        return self.driver.page_source

    def get_current_url(self):
        return self.driver.current_url