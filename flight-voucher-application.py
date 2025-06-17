from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, UnexpectedAlertPresentException

driver = webdriver.Chrome()
driver.get("https://altproexpo.com/flight-voucher-program/")

wait = WebDriverWait(driver, 15)
try:
    print("Checking for notification pop-up...")
    cancel_button = wait.until(EC.element_to_be_clickable((By.ID, "onesignal-slidedown-cancel-button")))
    cancel_button.click()
    print("Notification pop-up dismissed.")
except Exception:
    print("Notification pop-up not found, or already dismissed. Continuing script.")
    


# Fill basic form fields
driver.find_element(By.ID, "input_1_1").send_keys("Test")
driver.find_element(By.ID, "input_1_2").send_keys("Test")
driver.find_element(By.ID, "input_1_4").send_keys("test@zjevents.com")
driver.find_element(By.ID, "input_1_5").send_keys("0000000000")
driver.find_element(By.ID, "input_1_6").send_keys("Testing")
driver.find_element(By.ID, "input_1_7").send_keys("This is a test by Marcelo.")


# Try to submit the form
print("Attempting to submit the form...")
submit_button = wait.until(EC.element_to_be_clickable((By.ID, "gform_submit_button_1")))
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
