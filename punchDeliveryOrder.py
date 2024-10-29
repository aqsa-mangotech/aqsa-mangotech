from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize driver
chromedriver_path = "C:\\Users\\Lenovo\\Documents\\Aqsa\\Drivers\\chromedriver.exe"
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)

driver.maximize_window()
driver.get("https://restaurant.fougitodemo.com/")
driver.implicitly_wait(5)


# Function to place an order
def place_order():
    # Choose category
    time.sleep(5)
    btn_category = driver.find_element(By.XPATH, "//p[text()=' Treat ']")
    btn_category.click()

    # Choose item
    time.sleep(5)
    select_item = driver.find_element(By.CSS_SELECTOR, "svg.w-5.h-5")
    select_item.click()

    # Add to cart
    time.sleep(5)
    add_to_cart_btn = driver.find_element(By.XPATH, "//button[text()=' Add to cart ']")
    add_to_cart_btn.click()

    # Confirm order details
    time.sleep(5)
    confirm_items = driver.find_element(By.XPATH, "//button[text()=' Confirm Details ']")
    confirm_items.click()

    # Add user details
    phone_number = driver.find_element(By.ID, "phone")
    phone_number.send_keys("0507567600")
    time.sleep(2)

    first_name = driver.find_element(By.CSS_SELECTOR, "input[formcontrolname='customerFirstName']")
    first_name.send_keys("aqsa")

    email = driver.find_element(By.CSS_SELECTOR, "input[formcontrolname='email']")
    email.send_keys("test@gmail.com")

    address = driver.find_element(By.CSS_SELECTOR, "input[formcontrolname='AddressDetail']")
    address.send_keys("test address")

    # Confirm user details and place order
    confirm_details = driver.find_element(By.XPATH, "//button[text()='confirm']")
    confirm_details.click()
    time.sleep(5)


# Function to handle live location
def handle_live_location():
    time.sleep(6)
    point_cursor = driver.find_element(By.CSS_SELECTOR, "img.cursor-pointer.w-20")
    point_cursor.click()
    time.sleep(5)

    # Confirm location
    btn_confirm = driver.find_element(By.CSS_SELECTOR, "button.bg-gk-red.text-white")
    btn_confirm.click()


# Function to handle manual location input
def handle_manual_location():
    location_input = driver.find_element(By.ID, "addressInput")
    location_input.send_keys("dubai mall")

    suggestion = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'pac-item')]"))
    )
    suggestion.click()

    # Confirm location
    time.sleep(5)
    btn_confirm = driver.find_element(By.CSS_SELECTOR, "button.bg-gk-red.text-white")
    btn_confirm.click()


# Click "Order Here"
order_here = driver.find_element(By.CSS_SELECTOR, "div.font-Rubik.font-extrabold.text-white")
order_here.click()
time.sleep(2)

# Choose location method
live_location = True

if live_location:
    handle_live_location()
else:
    handle_manual_location()

# Place the order
place_order()
time.sleep(5)
# Close the driver
driver.quit()
