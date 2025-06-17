from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, UnexpectedAlertPresentException

# === Setup ===
driver = webdriver.Chrome()
driver.get("https://altproexpo.com/flight-approved/")

wait = WebDriverWait(driver, 20)

# === Dismiss notification popup === IF IT DOES NOT DEPLOY THE CODE CONTINUES
try:
    print("Checking for notification pop-up...")
    cancel_button = wait.until(EC.element_to_be_clickable(
        (By.ID, "onesignal-slidedown-cancel-button")
    ))
    cancel_button.click()
    print("Notification pop-up dismissed.")
except Exception:
    print("No notification pop-up or already dismissed.")

# === Fill form fields ===
driver.find_element(By.ID, "input_70_4").send_keys("Test")
driver.find_element(By.ID, "input_70_1_3").send_keys("Test")
driver.find_element(By.ID, "input_70_2").send_keys("test@zjevents.com")

# === Select show ===
wait.until(EC.element_to_be_clickable((By.ID, "choice_70_9_0"))).click()
print("Show selected.")

# === Select bringing someone? ===
wait.until(EC.element_to_be_clickable((By.ID, "choice_70_6_1"))).click()
print("Companion option selected: No")

# === UPLOAD FILE (manual step!) ===
print("\n=== ACTION REQUIRED ===")
print("Manually upload the file when browser is ready.")
print("Uploading 'Flight Voucher' file...")

# Wait for you to upload: check for file input value change
try:
    file_input = driver.find_element(By.ID, "input_70_5")
    print("Please manually select the file for Flight Voucher in the browser NOW.")
    WebDriverWait(driver, 90).until(
        lambda d: file_input.get_attribute("value") != ""
    )
    print("Flight Voucher file detected.")
except TimeoutException:
    print("File upload timed out. Please check manual upload.")



# === Submit form ===
print("Submitting the form...")
submit_button = wait.until(EC.element_to_be_clickable((By.ID, "gform_submit_button_70")))
submit_button.click()

# === Wait for submission or redirect ===
try:
    WebDriverWait(driver, 20).until(
        EC.url_changes(driver.current_url)
    )
    print("Form submitted successfully!")
except TimeoutException:
    print("Form submission may have failed or timed out.")

driver.quit()
