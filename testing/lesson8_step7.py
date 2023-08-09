import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

my_file = open("SomeFile.txt", "w+")
my_file.write('lolo')
my_file.close()

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")

firstName = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
firstName.send_keys("Daniil")

lastName = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
lastName.send_keys("Silenok")

mail = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
mail.send_keys('someMail.ru')

file_dir = os.path.abspath(os.path.dirname(__file__))
file_needed = os.path.join(file_dir, 'SomeFile.txt')
element = browser.find_element(By.CSS_SELECTOR, '#file')
element.send_keys(file_needed)
button = browser.find_element(By.CSS_SELECTOR, "button")
button.click()

time.sleep(10)

browser.quit()



