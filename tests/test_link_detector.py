from core.phishing_detector import PhishingDetector
from core.selenium_handler import SeleniumHandler

handler = SeleniumHandler("https://example.com")
handler.open()

detector = PhishingDetector(handler)
result = detector.run_all_checks()

print(result)

handler.close()