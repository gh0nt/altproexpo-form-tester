import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

try:
    driver = webdriver.Chrome()
    driver.maximize_window()
except Exception as e:
    print("Error setting up ChromeDriver. Make sure it's installed and in your PATH.")
    print(f"Error details: {e}")
    exit()

url = "https://altproexpo.com/become-a-partner/"
driver.get(url)

wait = WebDriverWait(driver, 15)

print(f"Successfully opened {url}")
print("\n--- IMPORTANT ---")
print("This form is protected by reCAPTCHA, which is designed to block bots.")
print("The script will click submit, but the submission is expected to fail.")
print("-----------------\n")

#Dismiss Notification Pop-up
try:
    print("Checking for notification pop-up...")
    cancel_button = wait.until(EC.element_to_be_clickable((By.ID, "onesignal-slidedown-cancel-button")))
    cancel_button.click()
    print("Notification pop-up dismissed.")
except Exception:
    print("Notification pop-up not found, or already dismissed. Continuing script.")


#Fill Form

try:
    print("Locating and filling form fields...")

    shows_legend = wait.until(EC.presence_of_element_located((By.ID, "field_62_9")))
    driver.execute_script("arguments[0].scrollIntoView(true);", shows_legend)
    time.sleep(0.5)

    wait.until(EC.element_to_be_clickable((By.ID, "choice_62_9_1"))).click() # Nashville 2025
    wait.until(EC.element_to_be_clickable((By.ID, "choice_62_9_2"))).click() # Houston 2025
    print("- Shows selected: Nashville, Houston")
    
    wait.until(EC.visibility_of_element_located((By.ID, "input_62_1_3"))).send_keys("Test")
    wait.until(EC.visibility_of_element_located((By.ID, "input_62_1_6"))).send_keys("TestLastName")
    wait.until(EC.visibility_of_element_located((By.ID, "input_62_4"))).send_keys("test@zjevents.com")
    wait.until(EC.visibility_of_element_located((By.ID, "input_62_5"))).send_keys("555-987-6543")
    print("- Personal details filled.")

    # wait.until(EC.visibility_of_element_located((By.ID, "input_62_21"))).send_keys("Florida")
    
    state_dropdown_element = wait.until(EC.visibility_of_element_located((By.ID, "input_62_21")))
    state = Select(state_dropdown_element)
    state.select_by_visible_text("Florida")
    print("- Location details filled (Florida).")
    
    country_dropdown_element = wait.until(EC.visibility_of_element_located((By.ID, "input_62_22")))
    country_select = Select(country_dropdown_element)
    country_select.select_by_visible_text("United States")
    print("- Location details filled (Florida, United States).")
    
    wait.until(EC.visibility_of_element_located((By.ID, "input_62_23"))).send_keys("ZJ Events") # Company Name
    wait.until(EC.visibility_of_element_located((By.ID, "input_62_49"))).send_keys("https://www.zjevents.com")
    print("- Company details filled.")
    
    how_heard_element = wait.until(EC.visibility_of_element_located((By.ID, "input_62_8")))
    how_heard_select = Select(how_heard_element)
    how_heard_select.select_by_value("Social Media")
    print("- 'How did you hear of us?' selected: Social Media")
    
    industry_legend = wait.until(EC.presence_of_element_located((By.ID, "field_62_10")))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", industry_legend)
    time.sleep(0.5)
    
    wait.until(EC.element_to_be_clickable((By.ID, "choice_62_10_2"))).click()
    wait.until(EC.element_to_be_clickable((By.ID, "choice_62_10_6"))).click()
    wait.until(EC.element_to_be_clickable((By.ID, "choice_62_10_13"))).click()
    print("- Industry types selected: CBD, Functional Beverage, Service Provider")
    
    comments_textarea = wait.until(EC.visibility_of_element_located((By.ID, "input_62_12")))
    comments_textarea.send_keys("This is an automated partnership inquiry using Selenium, developed by ZJ Events. Please disregard.")
    print("- Comments added.")

    print("\nForm has been filled successfully.")
    
    # Wait for submit button and ensure it's clickable
    submit_button = wait.until(EC.element_to_be_clickable((By.ID, "gform_submit_button_62")))
    
    # Scroll with offset to ensure button is below header
    driver.execute_script("""
        var element = arguments[0];
        var headerOffset = 100;
        var elementPosition = element.getBoundingClientRect().top;
        var offsetPosition = elementPosition + window.pageYOffset - headerOffset;
        window.scrollTo({
            top: offsetPosition,
            behavior: 'smooth'
        });
    """, submit_button)
    
    # Wait for scroll to complete
    time.sleep(2)
    
    print("Attempting to submit the form now...")
    
    # Try multiple click methods
    try:
        # Method 1: JavaScript click
        driver.execute_script("arguments[0].click();", submit_button)
    except Exception as e1:
        print(f"JavaScript click failed: {e1}")
        try:
            # Method 2: ActionChains
            actions = ActionChains(driver)
            actions.move_to_element(submit_button).pause(1).click().perform()
        except Exception as e2:
            print(f"ActionChains click failed: {e2}")
            try:
                # Method 3: Direct click with offset
                actions = ActionChains(driver)
                actions.move_to_element_with_offset(submit_button, 10, 10).click().perform()
            except Exception as e3:
                print(f"Offset click failed: {e3}")
                print("All click methods failed. Please check the form manually.")
    
    print("Submit button was clicked. Observe the website for reCAPTCHA errors.")
    time.sleep(10)

except Exception as e:
    print(f"\nAn error occurred while filling the form: {e}")

finally:
    print("TEST PASSED!!✅ Closing the browser.")
    driver.quit()