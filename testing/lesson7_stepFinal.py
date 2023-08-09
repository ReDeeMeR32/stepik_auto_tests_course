import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/get_attribute.html")

x_element = browser.find_element(By.CSS_SELECTOR, "img")
x = x_element.get_attribute("valuex")
y = calc(x)

element = browser.find_element(By.CSS_SELECTOR, '#answer')
element.send_keys(y)

checkbox = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
checkbox.click()

radiobutton = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
radiobutton.click()
time.sleep(5)

submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
submit.click()

time.sleep(10)
browser.quit()


