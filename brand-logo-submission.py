from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, UnexpectedAlertPresentException

driver = webdriver.Chrome()
driver.get("https://altproexpo.com/brand-logo-submission/")

wait = WebDriverWait(driver, 15)
try:
    print("Checking for notification pop-up...")
    cancel_button = wait.until(EC.element_to_be_clickable((By.ID, "onesignal-slidedown-cancel-button")))
    cancel_button.click()
    print("Notification pop-up dismissed.")
except Exception:
    print("Notification pop-up not found, or already dismissed. Continuing script.")
    


# Fill basic form fields
driver.find_element(By.ID, "input_47_5").send_keys("Test")
driver.find_element(By.ID, "input_47_1").send_keys("test@zjevents.com")

# File upload PLEASE ADD FILES BY YOURSELF
# The form is protected, so the submission will fail.





# About us and Industry Types
driver.find_element(By.ID, "input_47_6").send_keys("This is a test by Marcelo")
wait.until(EC.element_to_be_clickable((By.ID, "choice_47_9_5"))).click() # Energy enhancement
wait.until(EC.element_to_be_clickable((By.ID, "choice_47_9_1"))).click() # Accesories
print("- Shows selected: Energy enhancement, Accesories")

# Additional Information
driver.find_element(By.ID, "input_47_7").send_keys("test@zjevents.com")
driver.find_element(By.ID, "input_47_8").send_keys("0000000000")
driver.find_element(By.ID, "input_47_4").send_keys("https://www.zjevents.com")


# Now try to submit the form
print("Attempting to submit the form...")
submit_button = wait.until(EC.element_to_be_clickable((By.ID, "gform_submit_button_47")))
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
