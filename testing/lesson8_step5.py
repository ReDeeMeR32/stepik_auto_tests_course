import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/execute_script.html")

x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text
y = calc(x)

element = browser.find_element(By.CSS_SELECTOR, '.form-control')
element.send_keys(y)

checkbox = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
checkbox.click()

radiobutton = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
radiobutton.click()

submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
# browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
submit.click()

time.sleep(10)
browser.quit()


