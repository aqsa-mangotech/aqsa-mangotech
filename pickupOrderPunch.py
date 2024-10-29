from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chromedriver_path = "C:\\Users\\Lenovo\\Documents\\Aqsa\\Drivers\\chromedriver.exe"
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)

driver.maximize_window()
driver.get("https://restaurant.fougitodemo.com/")
driver.implicitly_wait(5)

#click order here
order_here = driver.find_element(By.CSS_SELECTOR, "div.font-Rubik.font-extrabold.text-white")
order_here.click()
time.sleep(6)

#switch to pickup button
btn_switch = driver.find_element(By.XPATH, "//p[text()='Switch To Pickup']")
btn_switch.click()
time.sleep(5)

#select any branch
select_branch = driver.find_element(By.XPATH, "(//button[text()=' select branch '])[2]") #choose branch
select_branch.click()

#chooses category
time.sleep(5)
btn_category = driver.find_element(By.XPATH, "//p[text()=' Treat ']")
time.sleep(5)
btn_category.click()

#choose items
time.sleep(5)
select_item = driver.find_element(By.CSS_SELECTOR, "svg.w-5.h-5")
select_item.click()

#add to cart
time.sleep(5)
click_item = driver.find_element(By.XPATH, "//button[text()=' Add to cart ']")
click_item.click()

# confirm order details
time.sleep(5)
confirm_items = driver.find_element(By.XPATH, "//button[text()=' Confirm Details ']")
confirm_items.click()

#add user details
phone_number = driver.find_element(By.ID,"phone")
phone_number.send_keys("0507567600")
time.sleep(5)

first_name = driver.find_element(By.CSS_SELECTOR,"input[formcontrolname='customerFirstName']")
first_name.send_keys("aqsa")
time.sleep(5)

email = driver.find_element(By.CSS_SELECTOR,"input[formcontrolname='email']")
email.send_keys("test@gmail.com")

#confirm user details and place order
confirm_details = driver.find_element(By.XPATH, "//button[text()='confirm']")
confirm_details.click()

time.sleep(5)
driver.quit()