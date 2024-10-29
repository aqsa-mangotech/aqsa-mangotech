from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver
chromedriver_path = "C:\\Users\\Lenovo\\Documents\\Aqsa\\Drivers\\chromedriver.exe"
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)

driver.maximize_window()
driver.get("https://restaurant.fougitodemo.com/")
driver.implicitly_wait(5)

# Click "Order Here"
order_here = driver.find_element(By.CSS_SELECTOR, "div.font-Rubik.font-extrabold.text-white")
order_here.click()
time.sleep(6)

# Switch to pickup button
btn_switch = driver.find_element(By.XPATH, "//p[text()='Switch To Pickup']")
btn_switch.click()
time.sleep(5)

# Select branch (e.g., Dubai branch 1 or Dubai branch 2)
branch_index = 1  # For second Dubai branch; change index for different branches

if branch_index == 2:
    select_branch = driver.find_element(By.XPATH, f"(//button[text()=' select branch '])[{branch_index}]")
    branch_name = "Karachi Branch"  # You can use this to distinguish between branches
else:
    select_branch = driver.find_element(By.XPATH, f"(//button[text()=' select branch '])[{branch_index}]")
    branch_name = "Dubai Branch"

select_branch.click()

# Branch-specific menu handling
if branch_name == "Karachi Branch":
    # Handle menu for Dubai Branch 1
    time.sleep(5)
    btn_category = driver.find_element(By.XPATH, "//p[text()=' Treat ']")  # Treat category for Branch 1
    time.sleep(5)
    btn_category.click()

    # Choose items for Branch 1
    time.sleep(5)
    select_item = driver.find_element(By.CSS_SELECTOR, "svg.w-5.h-5")
    select_item.click()

elif branch_name == "Dubai Branch":
    # Handle menu for Dubai Branch 2
    time.sleep(5)
    btn_category = driver.find_element(By.XPATH, "//p[text()=' Appetizers ']")  # Different category for Branch 2
    time.sleep(5)
    btn_category.click()

    # Choose items for Branch 2
    time.sleep(5)
    select_item = driver.find_element(By.CSS_SELECTOR, "svg.w-5.h-5")
    select_item.click()

# Add to cart
time.sleep(5)
click_item = driver.find_element(By.XPATH, "//button[text()=' Add to cart ']")
click_item.click()

# Confirm order details
time.sleep(5)
confirm_items = driver.find_element(By.XPATH, "//button[text()=' Confirm Details ']")
confirm_items.click()

# Add user details
phone_number = driver.find_element(By.ID, "phone")
phone_number.send_keys("0507567600")
time.sleep(5)

first_name = driver.find_element(By.CSS_SELECTOR, "input[formcontrolname='customerFirstName']")
first_name.send_keys("aqsa")
time.sleep(5)

email = driver.find_element(By.CSS_SELECTOR, "input[formcontrolname='email']")
email.send_keys("test@gmail.com")

# Confirm user details and place order
confirm_details = driver.find_element(By.XPATH, "//button[text()='confirm']")
confirm_details.click()

time.sleep(5)
driver.quit()
