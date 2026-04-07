from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException


class DOMDetector:
    def __init__(self, driver):
        self.driver = driver

    def analyze(self):
        dom_data = {
            "num_iframes": 0,
            "num_hidden_elements": 0,
            "num_scripts": 0,
            "dom_size": 0,
            "suspicious_flags": []
        }

        reasons = []

        # 1. iframes
        iframes = self.driver.find_elements(By.TAG_NAME, "iframe")
        dom_data["num_iframes"] = len(iframes)

        if len(iframes) > 0:
            dom_data["suspicious_flags"].append("Page contains iframes")
            reasons.append("Page contains iframe elements")

        # 2. hidden elements
        all_elements = self.driver.find_elements(By.XPATH, "//*")[:1000]
        dom_data["dom_size"] = len(all_elements)

        hidden_count = 0

        for el in all_elements:
            try:
                if not el.is_displayed():
                    hidden_count += 1
            except StaleElementReferenceException:
                continue

        dom_data["num_hidden_elements"] = hidden_count

        if hidden_count > 20:
            dom_data["suspicious_flags"].append("Too many hidden elements")
            reasons.append("High number of hidden elements detected")

        # 3. scripts
        scripts = self.driver.find_elements(By.TAG_NAME, "script")
        dom_data["num_scripts"] = len(scripts)

        if len(scripts) > 50:
            dom_data["suspicious_flags"].append("Too many scripts")
            reasons.append("High number of script tags detected")

        # 🔥 SCORING (UNCHANGED)
        score = 0

        if dom_data["num_iframes"] > 3:
            score += 1
            reasons.append("Excessive iframe usage")

        if dom_data["num_hidden_elements"] > 100:
            score += 1
            reasons.append("Too many hidden elements (high risk)")

        if dom_data["num_scripts"] > 150:
            score += 1
            reasons.append("Too many scripts (possible obfuscation)")

        if dom_data["dom_size"] > 5000:
            score += 1
            reasons.append("Very large DOM size")

        # 🔹 KEEP ORIGINAL RETURN (no break)
        return score, dom_data

    # 🔥 NEW (optional, future use)
    def get_detailed_result(self):
        dom_data = {
            "num_iframes": 0,
            "num_hidden_elements": 0,
            "num_scripts": 0,
            "dom_size": 0,
            "suspicious_flags": []
        }

        reasons = []
        score = 0

        # 1. iframes
        iframes = self.driver.find_elements(By.TAG_NAME, "iframe")
        dom_data["num_iframes"] = len(iframes)

        if len(iframes) > 0:
            dom_data["suspicious_flags"].append("Page contains iframes")
            reasons.append("Page contains iframe elements")

        if dom_data["num_iframes"] > 3:
            score += 1
            reasons.append("Excessive iframe usage")

        # 2. hidden elements
        all_elements = self.driver.find_elements(By.XPATH, "//*")[:1000]
        dom_data["dom_size"] = len(all_elements)

        hidden_count = 0

        for el in all_elements:
            try:
                if not el.is_displayed():
                    hidden_count += 1
            except StaleElementReferenceException:
                continue

        dom_data["num_hidden_elements"] = hidden_count

        if hidden_count > 20:
            dom_data["suspicious_flags"].append("Too many hidden elements")
            reasons.append("High number of hidden elements detected")

        if hidden_count > 100:
            score += 1
            reasons.append("Too many hidden elements (high risk)")

        # 3. scripts
        scripts = self.driver.find_elements(By.TAG_NAME, "script")
        dom_data["num_scripts"] = len(scripts)

        if len(scripts) > 50:
            dom_data["suspicious_flags"].append("Too many scripts")
            reasons.append("High number of script tags detected")

        if dom_data["num_scripts"] > 150:
            score += 1
            reasons.append("Too many scripts (possible obfuscation)")

        # DOM size
        if dom_data["dom_size"] > 5000:
            score += 1
            reasons.append("Very large DOM size")

        return {
            "score": score,
            "reasons": reasons,
            "data": dom_data
        }