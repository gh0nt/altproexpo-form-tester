# 🛠️ AltProExpo‑Form‑Tester

Automated testing tool for the Alt Pro Expo buyer‑registration form using Selenium & Python.

---

## 🔍 Overview

This lightweight Python script automates form submission on the Alt Pro Expo Gravity Forms page (`/meet-the-buyer/buyer-registration/`).  
Ideal for QA teams or developers needing to validate form behavior—especially when workflows include file uploads, geolocation, “plus one” conditional logic, and payment fields.

---

## ⚙️ Features

- Opens Chrome and navigates to the registration page  
- Handles dynamic UI elements (pop-ups, date pickers, geolocation, etc.)  
- Fills **all required fields**: personal info, address, phone, ID, plus‑one info, payment details  
- Uploads a company logo with file-size validation  
- Conditional plus‑one section (only if “Yes” is selected)  
- Submits the form and confirms success or timeout

---

## 🔧 Prerequisites

- **Python 3.10+**  
- **Google Chrome**  
- **ChromeDriver** (matching your Chrome version)  
- **Selenium**: install via pip  
  ```bash
  pip install selenium

---
## 🧪 How to Use
Clone the repo:
```
bash
Copy code
git clone https://github.com/gh0nt/altproexpo-form-tester.git
cd altproexpo-form-tester
```
Add your test logo:

Save it under ./fixtures/ (e.g. logo.png)

Ensure the script’s logo_path variable matches your filename

Update form values:

```Edit test_registration.py to set realistic test data (name, email, phone, job title, etc.) ```

Run the script:

bash

Copy code
```
python test_registration.py
```
Observe console output:
```
✅ Form submitted successfully (if redirected)

⚠️ Timeout (if submission failed or hung)

📁 Script Breakdown
```
### The core script does:

- Imports: selenium, WebDriverWait, EC, etc.

- Setup: launches Chrome and opens the form URL

- Waits & Fills:

- Personal information (name, email, phone, job title)

- Address fields (street, city, province, country, postal code)

- File upload for logo

- Date picker and payment details (number, expiry, CVC, cardholder name)

- Optional plus‑one section

- Submit: waits for URL redirect or logs a timeout 

## ✅ File Uploads
Gravity Forms limits logo files to 25 MB. The script simulates the input only and does not bypass CAPTCHA or IP restrictions.
Validation errors can still occur on submission—this is expected in real-world testing.

## 🛠️ Customization Tips
- Modify the path for chromedriver/web driver if needed
- Sync with updated Gravity Forms if field IDs change
- Add environment-based test data via .env or separate config

Integrate into CI pipelines (e.g. GitHub Actions) for regression testing

## 🧠 FAQ
Q: Can this bypass CAPTCHAs or 2FA?
A: No—those require manual interaction or external bypass services.

Q: What if the form layout changes?
A: Update the element locators (IDs/XPaths) in test_registration.py.

👥 Contribute
Contributions welcome—open issues or PRs for:

Enhanced error handling

Configurable test data from env/config

CI pipeline integration (GitHub Actions, etc.)

📄 License
No LICENSE file included in repo. Consider adding one for open-source use.

yaml
Copy code

---


