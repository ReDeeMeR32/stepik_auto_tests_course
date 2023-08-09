import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/alert_accept.html")


browser.find_element(By.CSS_SELECTOR, 'button').click()

alert = browser.switch_to.alert
alert.accept()

x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
x = x_element.text
result = calc(x)
put = browser.find_element(By.CSS_SELECTOR, '.form-control')
put.send_keys(result)
browser.find_element(By.CSS_SELECTOR, 'button').click()

time.sleep(10)
browser.quit()

