import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, UnexpectedAlertPresentException

driver = webdriver.Chrome()
driver.get("https://altproexpo.com/advertising-assets/")

wait = WebDriverWait(driver, 15)
try:
    print("Checking for notification pop-up...")
    cancel_button = wait.until(EC.element_to_be_clickable((By.ID, "onesignal-slidedown-cancel-button")))
    cancel_button.click()
    print("Notification pop-up dismissed.")
except Exception:
    print("Notification pop-up not found, or already dismissed. Continuing script.")

# Fill basic form fields
driver.find_element(By.ID, "input_25_1").send_keys("test@example.com")
driver.find_element(By.ID, "input_25_5").send_keys("Test Company")
driver.find_element(By.ID, "choice_25_9_0").click()  # Email option

# Get the absolute path of the email file
email_file_path = os.path.abspath("test-files/test_email.jpg")

print("Uploading email file...")
# Wait for and find the file input
file_input = WebDriverWait(driver, 10).until(
    lambda d: d.find_element(By.CSS_SELECTOR, "#gform_multifile_upload_25_4 input[type='file']")
)
driver.execute_script("arguments[0].style.display = 'block';", file_input)

# Upload the file
file_input.send_keys(email_file_path)
print(f"File '{email_file_path}' sent for upload.")

# Wait for the file to appear in the preview
print("Waiting for file upload to complete...")
try:
    WebDriverWait(driver, 30).until(
        lambda d: len(d.find_elements(By.CSS_SELECTOR, "#gform_preview_25_4 .ginput_preview")) > 0
    )
    print("File upload completed successfully.")
except TimeoutException:
    print("Timeout waiting for file upload to complete.")

# Wait a bit to ensure the upload is fully processed
time.sleep(2)

# Handle any alerts that might appear
try:
    alert = driver.switch_to.alert
    if "Please wait for the uploading to complete" in alert.text:
        print("Waiting for upload to complete...")
        time.sleep(5)  # Wait for upload to complete
    alert.accept()
except:
    pass

# Now try to submit the form
print("Attempting to submit the form...")
submit_button = wait.until(EC.element_to_be_clickable((By.ID, "gform_submit_button_25")))
submit_button.click()

# Wait for form submission
try:
    WebDriverWait(driver, 20).until(
        EC.url_changes(driver.current_url)
    )
    print("Form submitted successfully!")
except TimeoutException:
    print("Form submission might have failed or timed out.")

driver.quit()
