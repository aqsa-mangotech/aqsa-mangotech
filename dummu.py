from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

chromedriver_path = "C:\\Users\\Lenovo\\Documents\\Aqsa\\Drivers\\chromedriver.exe"
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)

driver.maximize_window()
driver.get("https://restaurant.fougitodemo.com/dinein/100/20085?id=restaurant.fougitodemo.com")
driver.implicitly_wait(5)

# choose category
time.sleep(6)
btn_category = driver.find_element(By.XPATH, "//p[text()=' Treat ']")
time.sleep(3)
btn_category.click()

# Choose item
time.sleep(10)
btn_selected = driver.find_element(By.XPATH, "//h1[text()='chocolates']")

# Scroll the element into view and try clicking it
try:
    # Scroll the element into view
    driver.execute_script("arguments[0].scrollIntoView(true);", btn_selected)
    time.sleep(2)  # Allow time for scrolling

    # Attempt to click the element
    btn_selected.click()
    print("Successfully clicked the item using the .click() method.")

except Exception as e:
    print(f"Standard click failed, trying JavaScript click: {e}")

    try:
        # If .click() fails, use JavaScript to force the click
        driver.execute_script("arguments[0].click();", btn_selected)
        print("Successfully clicked the item using JavaScript.")
    except Exception as e2:
        print(f"Failed to click the item using JavaScript as well: {e2}")

# add to cart
time.sleep(2)
click_item = driver.find_element(By.XPATH, "//button[text()=' Add to cart ']")
click_item.click()

# confirm order details
time.sleep(2)
confirm_items = driver.find_element(By.XPATH, "//button[text()=' Confirm Details ']")
confirm_items.click()

# add user details
phone_number = driver.find_element(By.ID, "phone")
phone_number.send_keys("0507567600")
time.sleep(5)

first_name = driver.find_element(By.CSS_SELECTOR, "input[formcontrolname='customerFirstName']")
first_name.send_keys("aqsa")
time.sleep(5)

# confirm user details and place order
confirm_details = driver.find_element(By.XPATH, "//button[text()='confirm']")
confirm_details.click()


time.sleep(5)
driver.quit()






