from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.saucedemo.com/")

username = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.NAME, "password")
login = driver.find_element(By.ID, "login-button")

username.send_keys("standard_user")
password.send_keys("secret_sauce")

print(username.get_attribute("placeholder"))
print(login.is_enabled())
print(username.is_displayed())

login.click()

products = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
print("\nEntire Product List:")
for index, product in enumerate(products, 1):
    print(f"{index}. {product.text}")

input("\nPress Enter in the VS Code terminal to close the browser...")
driver.quit()
