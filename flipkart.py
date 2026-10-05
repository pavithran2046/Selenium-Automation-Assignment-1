from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()
driver.maximize_window()

driver.get("https://www.flipkart.com/login")

wait = WebDriverWait(driver, 10)

try:
    wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Use Email-ID')]")))

    try:
        phone_input = driver.find_element(
            By.XPATH, "//*[contains(text(), 'Use Email-ID')]/preceding::input[1]"
        )
    except Exception:
        all_inputs = driver.find_elements(By.TAG_NAME, "input")
        phone_input = None
        for inp in all_inputs:
            name = inp.get_attribute("name") or ""
            cls = inp.get_attribute("class") or ""
            placeholder = (inp.get_attribute("placeholder") or "").lower()
            if name != "q" and "pke_ee" not in cls.lower() and "search" not in placeholder:
                phone_input = inp
                break

    if not phone_input:
        raise Exception("Could not find the phone number input element.")

    phone_input.click()
    phone_input.clear()
    phone_input.send_keys("7812817889")
    print("Mobile number entered into the phone field.")

    continue_btn = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(., 'Continue')]")
        )
    )
    continue_btn.click()
    print("Clicked Continue button.")

    input("\nPlease enter the OTP in the Edge browser window, then press Enter here...")
    print("Current URL:", driver.current_url)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    input("\nPress Enter in the terminal to close Edge...")
    driver.quit()