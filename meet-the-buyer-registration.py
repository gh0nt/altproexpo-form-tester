from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# === CONFIG ===
URL = "https://altproexpo.com/meet-the-buyer/buyer-registration/"
UPLOAD_FILE_PATH = r"C:\path\to\your\logo.jpg"  

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)
driver.get(URL)

# === Fill Personal Info ===
wait.until(EC.visibility_of_element_located((By.ID, "input_60_4_3"))).send_keys("Johny")
driver.find_element(By.ID, "input_60_4_6").send_keys("Test")
driver.find_element(By.ID, "input_60_6").send_keys("test@zjevents.com")
driver.find_element(By.ID, "input_60_7").send_keys("1234567890")
driver.find_element(By.ID, "input_60_5").send_keys("Tester")

# === Fill Company Info ===
driver.find_element(By.ID, "input_60_8").send_keys("ZJ Events")
driver.find_element(By.ID, "input_60_10").send_keys("0987654321")
driver.find_element(By.ID, "input_60_9_1").send_keys("123 Main Street")
driver.find_element(By.ID, "input_60_9_2").send_keys("Suite 100")
driver.find_element(By.ID, "input_60_9_3").send_keys("New York")
driver.find_element(By.ID, "input_60_9_4").send_keys("NY")
driver.find_element(By.ID, "input_60_9_5").send_keys("10001")
country_select = driver.find_element(By.ID, "input_60_9_6")
for option in country_select.find_elements(By.TAG_NAME, "option"):
    if option.text == "United States":
        option.click()
        break

# === Company Logo Upload ===
logo_input = driver.find_element(By.ID, "input_60_40")
try:
    # Try direct upload
    logo_input.send_keys(UPLOAD_FILE_PATH)
    print("File upload attempted with send_keys.")
except Exception:
    print("If send_keys is blocked by the site, upload manually.")
    input("Please upload the logo manually in the browser then press Enter here...")

# === Company Website ===
driver.find_element(By.ID, "input_60_41").send_keys("https://example.com")

# === Flight Booking Info ===
driver.find_element(By.ID, "input_60_12_1").send_keys("456 Office Blvd")
driver.find_element(By.ID, "input_60_12_2").send_keys("Floor 3")
driver.find_element(By.ID, "input_60_12_3").send_keys("Chicago")
driver.find_element(By.ID, "input_60_12_4").send_keys("IL")
driver.find_element(By.ID, "input_60_12_5").send_keys("60601")
country_select = driver.find_element(By.ID, "input_60_12_6")
for option in country_select.find_elements(By.TAG_NAME, "option"):
    if option.text == "United States":
        option.click()
        break

# === Date of Birth ===
driver.find_element(By.ID, "input_60_26").send_keys("01/01/1980")

# === Preferred Airport ===
driver.find_element(By.ID, "input_60_13").send_keys("ORD")

# === Type of ID ===
driver.find_element(By.ID, "choice_60_28_0").click()  # Passport

# === ID Number ===
driver.find_element(By.ID, "input_60_31").send_keys("A12345678")

# === Plus One ===
driver.find_element(By.ID, "choice_60_15_1").click()  # No

# === Credit Card Info ===
driver.find_element(By.ID, "input_60_33").send_keys("4111111111111111")
month_select = driver.find_element(By.ID, "input_60_37")
month_select.find_element(By.XPATH, ".//option[text()='January']").click()
year_select = driver.find_element(By.ID, "input_60_38")
year_select.find_element(By.XPATH, ".//option[text()='2026']").click()
driver.find_element(By.ID, "input_60_39").send_keys("123")
driver.find_element(By.ID, "input_60_35").send_keys("John Doe")

# === Submit ===
submit_btn = wait.until(EC.element_to_be_clickable((By.ID, "gform_submit_button_60")))
submit_btn.click()

print("Form submitted. Check for confirmation on the page.")
