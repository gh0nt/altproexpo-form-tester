from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, UnexpectedAlertPresentException

driver = webdriver.Chrome()
driver.get("https://altproexpo.com/become-a-media-partner/")

wait = WebDriverWait(driver, 15)
try:
    print("Checking for notification pop-up...")
    cancel_button = wait.until(EC.element_to_be_clickable((By.ID, "onesignal-slidedown-cancel-button")))
    cancel_button.click()
    print("Notification pop-up dismissed.")
except Exception:
    print("Notification pop-up not found, or already dismissed. Continuing script.")
    
# Select Shows Checkboxes 
wait.until(EC.element_to_be_clickable((By.ID, "choice_3_8_1"))).click() # Nashville 2025
wait.until(EC.element_to_be_clickable((By.ID, "choice_3_8_2"))).click() # Houston 2025
print("- Shows selected: Nashville, Houston")

# Fill basic form fields
driver.find_element(By.ID, "input_3_1").send_keys("Test")
driver.find_element(By.ID, "input_3_2").send_keys("Testing")
driver.find_element(By.ID, "input_3_4").send_keys("test@example.com")
driver.find_element(By.ID, "input_3_3").send_keys("0000000000")
driver.find_element(By.ID, "input_3_5").send_keys("IT / ZJ Events")
driver.find_element(By.ID, "input_3_9").send_keys("https://www.zjevents.com")
driver.find_element(By.ID, "input_3_7").send_keys("This is a test by Marcelo")



# Now try to submit the form
print("Attempting to submit the form...")
submit_button = wait.until(EC.element_to_be_clickable((By.ID, "gform_submit_button_3")))
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
