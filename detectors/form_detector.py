from selenium.webdriver.common.by import By
from urllib.parse import urlparse


class FormDetector:

    def __init__(self, handler):
        self.handler = handler
        self.driver = handler.driver
        self.base_domain = urlparse(handler.get_current_url()).netloc

    def has_password_field(self):
        return len(self.driver.find_elements(By.XPATH, "//input[@type='password']")) > 0

    def form_submits_to_external(self):
        forms = self.driver.find_elements(By.TAG_NAME, "form")

        for form in forms:
            action = form.get_attribute("action")

            if action:
                parsed = urlparse(action)

                # external domain
                if parsed.netloc and self.base_domain not in parsed.netloc:
                    return True

        return False

    def has_suspicious_action(self):
        forms = self.driver.find_elements(By.TAG_NAME, "form")

        for form in forms:
            action = form.get_attribute("action")

            if action:
                if action == "" or action.startswith("javascript"):
                    return True

        return False

    def has_multiple_forms(self):
        return len(self.driver.find_elements(By.TAG_NAME, "form")) > 2

    def analyze(self):
        score = 0
        reasons = []

        if self.has_password_field():
            score += 2
            reasons.append("Page contains password input field")

        if self.form_submits_to_external():
            score += 5
            reasons.append("Form submits data to external domain")

        if self.has_suspicious_action():
            score += 2
            reasons.append("Form has suspicious or empty action")

        if self.has_multiple_forms():
            score += 1
            reasons.append("Multiple forms detected on page")

        # 🔹 KEEP ORIGINAL RETURN (no break)
        return score

    # 🔥 NEW (optional, future use)
    def get_detailed_result(self):
        score = 0
        reasons = []

        if self.has_password_field():
            score += 2
            reasons.append("Page contains password input field")

        if self.form_submits_to_external():
            score += 5
            reasons.append("Form submits data to external domain")

        if self.has_suspicious_action():
            score += 2
            reasons.append("Form has suspicious or empty action")

        if self.has_multiple_forms():
            score += 1
            reasons.append("Multiple forms detected on page")

        return {
            "score": score,
            "reasons": reasons
        }