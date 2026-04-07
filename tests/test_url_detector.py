from selenium import webdriver
from core.handler import UniversalWebHandler
from core.phishing_detector import PhishingDetector
from detectors.url_detector import URLDetector

driver = webdriver.Chrome()

# 🔴 Use ONE URL everywhere
url = "https://www.youtube.com/"

# URL detector test
detector = URLDetector(url)
score, features = detector.get_url_score()

print("Features:", features)
print("Score:", score)

# Full system test
handler = UniversalWebHandler(driver)
handler.open_url(url)

detector = PhishingDetector(handler)
result = detector.run_all_checks()

print(result)

driver.quit()