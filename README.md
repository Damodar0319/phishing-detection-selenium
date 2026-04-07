# 🧠 AI Phishing Detection System (Selenium-Based)

A real-time phishing detection web application that analyzes live websites using **Selenium-based web scraping** and classifies them based on URL patterns, DOM structure, links, and form behavior.

---

## 🚀 Features

* 🔍 Real-time website analysis using Selenium
* 🌐 Phishing detection based on:

  * URL structure
  * DOM elements
  * Links & anchor mismatches
  * Form behavior
* ⚖️ Weighted scoring system
* 🧠 Explainable results (clear reasons for detection)
* 📊 Confidence score & risk classification
* 🌐 Interactive Flask web interface
* 📂 Bulk URL scanning via CSV

---

## 🏗️ Project Structure

```
phishing-detector/
│
├── core/               # Core logic & driver setup
├── detectors/          # URL, DOM, Link, Form detectors
├── engine/             # Scoring & decision engine
├── reports/            # Report generation
├── webapp/             # Flask web app
│   ├── static/         # CSS & JavaScript
│   ├── templates/      # HTML UI
│   └── app.py
│
├── data/               # Input datasets (CSV)
├── tests/              # Testing scripts
├── main.py             # CLI entry point
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

```bash
git clone <your-repo-link>
cd phishing-detector
pip install -r requirements.txt
```

---

## ▶️ Run Web App (IMPORTANT)

⚠️ Make sure you are in the **project root directory**

### ✅ Correct way to run:

```bash
python -m webapp.app
```

---

### 🌐 Open in browser:

```
http://127.0.0.1:5000
```

---

### ❗ Common Mistake

Do NOT run:

```bash
python webapp/app.py
```

This may cause import errors due to the modular project structure.

---

## 🧪 Run CLI (Single URL)

```bash
python main.py
```

---

## 📊 Bulk Scan (CSV)

Create a CSV file inside the `data/` folder:

```
url
https://google.com
http://fake-login.xyz
```

Then run your batch processing logic (if implemented in CLI or script).

---

## 🧠 How It Works

1. Selenium loads the target website
2. The system extracts:

   * URL features
   * DOM structure
   * Links
   * Forms
3. Each detector assigns a score
4. Scores are combined using a weighted scoring system
5. Final output includes:

   * Verdict (Safe / Suspicious / Phishing)
   * Threat score
   * Confidence
   * Reasons for classification

---

## 💡 Example Output

```json
{
  "final_score": 9.5,
  "verdict": "High Risk",
  "confidence": 0.95,
  "reasons": [
    "Form submits data to external domain",
    "URL contains '@' symbol"
  ]
}
```

---

## 🛠️ Tech Stack

* Python
* Selenium
* Flask
* HTML / CSS / JavaScript

---

## 📈 Future Improvements

* Machine Learning integration
* Dataset-based training
* API deployment
* Browser extension
* Cloud deployment

---

## 📸 Demo (Recommended)

Add screenshots or a demo GIF here to showcase your UI and results.

---

## 👨‍💻 Author

**Y Venkata Damodar**

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
