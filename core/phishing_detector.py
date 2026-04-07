from detectors.dom_detector import DOMDetector
from detectors.link_detector import LinkDetector
from detectors.url_detector import URLDetector
from detectors.form_detector import FormDetector
from reports.report_generator import ReportGenerator


class PhishingDetector:

    def __init__(self, handler):
        self.handler = handler

    def run_all_checks(self):
        driver = self.handler.driver
        url = self.handler.get_current_url()

        # 🔹 Check if page is reachable
        unreachable = False
        try:
            _ = driver.title
        except Exception:
            unreachable = True

        # 🔹 Run detectors (DETAILED MODE)
        dom_result = DOMDetector(driver).get_detailed_result()
        link_result = LinkDetector(driver, url).get_detailed_result()
        url_result = URLDetector(url).get_detailed_result()
        form_result = FormDetector(self.handler).get_detailed_result()

        # 🔹 Combine scores
        final_score = (
            (dom_result["score"] * 0.5) +
            (link_result["score"] * 1) +
            (url_result["score"] * 2) +
            (form_result["score"] * 1.5)
        )

        # 🔹 Collect ALL reasons
        reasons = []
        reasons.extend(dom_result["reasons"])
        reasons.extend(link_result["reasons"])
        reasons.extend(url_result["reasons"])
        reasons.extend(form_result["reasons"])

        if unreachable:
            final_score += 2
            reasons.append("Page is unreachable")

        # 🔹 Remove duplicate reasons
        reasons = list(set(reasons))

        # 🔹 Whitelist adjustment
        trusted_domains = ["google.com", "amazon.com", "wikipedia.org"]
        if any(domain in url for domain in trusted_domains):
            final_score = max(0, final_score - 3)

        # 🔹 Classification (IMPROVED BUT SAME STYLE)
        if final_score >= 10:
            verdict = "Phishing"
        elif final_score >= 7:
            verdict = "High Risk"
        elif final_score >= 4:
            verdict = "Suspicious"
        else:
            verdict = "Legit"

        # 🔹 Confidence
        confidence = round(min(final_score / 10, 1.0), 2)

        # 🔹 Feature mapping (for ReportGenerator compatibility)
        features = url_result["features"]
        features["unreachable"] = unreachable

        # 🔹 Report generation
        report_gen = ReportGenerator(
            url=url,
            features=features,
            score=final_score,
            classification=verdict,
            extra_reasons=reasons
        )

        report = report_gen.generate()

        # 🔹 Final output
        return {
            "final_score": round(final_score, 2),
            "verdict": verdict,
            "confidence": confidence,
            "reasons": reasons,
            "report": report,

            # 🔥 Detailed breakdown (VERY IMPRESSIVE)
            "breakdown": {
                "DOM": dom_result,
                "LINK": link_result,
                "URL": url_result,
                "FORM": form_result
            }
        }