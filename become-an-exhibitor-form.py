import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Setup WebDriver 

try:
    driver = webdriver.Chrome()
    driver.maximize_window() 
except Exception as e:
    print("Error setting up ChromeDriver. Make sure it's installed and in your PATH.")
    print(f"Error details: {e}")
    exit()

url = "https://altproexpo.com/become-an-exhibitor/"
driver.get(url)

wait = WebDriverWait(driver, 15)


try:
    print(f"Successfully opened {url}")

 
    print("Locating and filling form fields...")
    shows_legend = wait.until(EC.presence_of_element_located((By.XPATH, "//legend[contains(text(), 'Which Show(s)')]")))
    driver.execute_script("arguments[0].scrollIntoView(true);", shows_legend)
    time.sleep(0.5) 

    # Select Shows Checkboxes 
    wait.until(EC.element_to_be_clickable((By.ID, "choice_44_9_1"))).click() # Nashville 2025
    wait.until(EC.element_to_be_clickable((By.ID, "choice_44_9_2"))).click() # Houston 2025
    print("- Shows selected: Nashville, Houston")

    # Fill Name, Email, and Phone
    wait.until(EC.visibility_of_element_located((By.ID, "input_44_1_3"))).send_keys("Test")
    wait.until(EC.visibility_of_element_located((By.ID, "input_44_1_6"))).send_keys("Test")
    wait.until(EC.visibility_of_element_located((By.ID, "input_44_4"))).send_keys("test@zjevents.com")
    wait.until(EC.visibility_of_element_located((By.ID, "input_44_5"))).send_keys("555-123-4567")
    print("- Personal details filled.")

    #Fill Company Info
    wait.until(EC.visibility_of_element_located((By.ID, "input_44_23"))).send_keys("Test")
    wait.until(EC.visibility_of_element_located((By.ID, "input_44_59"))).send_keys("https://www.example.com")
    print("- Company details filled.")
    
    # Fill Questions
    comments_textarea = wait.until(EC.visibility_of_element_located((By.ID, "input_44_12")))
    comments_textarea.send_keys("This is an automated test inquiry using Selenium, developed by ZJ Events. Please disregard.")
    print("- Comments added.")

    # Handle Email Updates Checkbox 
 
    email_updates_checkbox = wait.until(EC.presence_of_element_located((By.ID, "choice_44_27_1")))
    if email_updates_checkbox.is_selected():
        print("- 'Email Updates' is checked by default. Leaving as is.")
    print("\nForm has been filled successfully.")
    
    
    
    print("Submitting form...")
    
    
    submit_button = wait.until(EC.element_to_be_clickable((By.ID, "gform_submit_button_44")))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit_button)
    time.sleep(1)  
    

    try:
        driver.execute_script("arguments[0].click();", submit_button)
    except Exception as e:
        print(f"JavaScript click failed, trying alternative method: {e}")
        # Alternative method: move to element and click
        actions = ActionChains(driver)
        actions.move_to_element(submit_button).click().perform()
    
   
    try:

        success_message = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "gform_confirmation_message")))
        print("Form submitted successfully!")
    except Exception as e:
        print(f"Error during form submission: {e}")
        print("Please check if the form was actually submitted.")

    print("Script finished. Closing the browser.")


except Exception as e:
    print(f"\nAn error occurred while filling the form: {e}")

finally:

    print("Script finished. Closing the browser.")
    driver.quit()