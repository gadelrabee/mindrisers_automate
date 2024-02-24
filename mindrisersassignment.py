import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#this line of code doestnot work in this project because we have used x-path method to located elements

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def is_valid_email(email):
    try:
        email_pattern = "^[a-z]=[\.]?[a-z 0-9]+[@]\w+{2,3}$"

        if re.search(email_pattern,email):
             return True

        else:
             return False

    except Exception as e:
        print(e)
        return False
def is_valid_phone(phone):
    return bool(re.match(r'^\{10}$', phone))

def is_name_valid(name):
    return bool(re.match("^[A-Za-z]+(?:[-\s'][A-Za-z]+)*$", name))

driver.get("https://mindrisers.com.np/contact-us")
driver.maximize_window()
page_height = driver.execute_script("return document.body.scrollHeight")
scroll_speed = 200   # Adjust this value to control scrolling speed
scroll_iterations = int(page_height / scroll_speed)
for _ in range(scroll_iterations):
    driver.execute_script(f"window.scrollBy(0, {scroll_speed});")
    time.sleep(1)

name_field = driver.find_element(*(By.XPATH,"//input[@placeholder='Name']"))

email_field = driver.find_element(*(By.XPATH,"//input[@placeholder='Email']"))

phone_field = driver.find_element(*(By.XPATH,"//input[@placeholder='Phone']"))

subject_field = driver.find_element(*(By.XPATH,"//input[@placeholder='Subject']"))

any_queries_field = driver.find_element(*(By.XPATH,"//textarea[@placeholder='Queries']"))

name = "Pritam Waiba"
email = "waibapritam1234@@gmail.com"
phone = "1234567890"
subject = "Quality Assurance"
any_queries = "This is a test message."
time.sleep(2)

if not name:
    print("Name cannot be empty.")
name_field.clear()
name_field.send_keys(name)
time.sleep(4)

if is_valid_email(email):
    print("Valid email address")
else:
    print("Invalid email address")
email_field.clear()
email_field.send_keys(email)
time.sleep(4)

if not phone:
    print("Phone number cannot be empty")
phone_field.clear()
phone_field.send_keys(phone)
time.sleep(4)

if not subject:
    print("Subject cannot be empty")
subject_field.clear()
subject_field.send_keys(subject)
time.sleep(4)

any_queries_field.clear()
any_queries_field.send_keys(any_queries)
time.sleep(3)

driver.quit()
print("Congrats!! code executed successfully")


