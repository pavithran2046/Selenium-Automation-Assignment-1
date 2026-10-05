from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Edge()

driver.maximize_window()

try:
    driver.get("https://www.bing.com")
    
    time.sleep(2)

    search_box = driver.find_element(By.ID, "sb_form_q")

    search_box.send_keys("Suriya actor")
    search_box.send_keys(Keys.RETURN)

    time.sleep(3)

    print("Search Result Page Title:", driver.title)

    results = driver.find_elements(By.CSS_SELECTOR, "li.b_algo h2 a")
    print("\nTop Search Results:")
    
    count = 1
    for result in results:
        title = result.text.strip()
        url = result.get_attribute("href")
        
        if title and url:
            print(f"{count}. {title}")
            print(f"   Link: {url}\n")
            count += 1
            if count > 5:
                break

except Exception as e:
    print("An error occurred during execution:", e)

finally:
    input("\nPress Enter in the VS Code terminal to close the browser...")
    driver.quit()
