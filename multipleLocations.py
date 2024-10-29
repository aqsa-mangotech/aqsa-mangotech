from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chromedriver_path = "C:\\Users\\Lenovo\\Documents\\Aqsa\\Drivers\\chromedriver.exe"
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)

driver.maximize_window()
driver.get("https://restaurant.fougitodemo.com/")
driver.implicitly_wait(5)

order_here = driver.find_element(By.CSS_SELECTOR, "div.font-Rubik.font-extrabold.text-white")
order_here.click()
time.sleep(6)

live_location = True

if live_location:
        time.sleep(6)
        point_cursor = driver.find_element(By.CSS_SELECTOR, "img.cursor-pointer.w-20")
        time.sleep(6)
        point_cursor.click()
        time.sleep(5)
else:
        location_input = driver.find_element(By.ID,"addressInput")
        location_input.send_keys("dubai mall")
        suggestion = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'pac-item')]"))  # Adjust this selector
        )

        suggestion.click()

time.sleep(5)
time.sleep(5)
driver.quit()