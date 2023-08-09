import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/redirect_accept.html")


browser.find_element(By.CSS_SELECTOR, 'button').click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
result = calc(x_element.text)


put = browser.find_element(By.CSS_SELECTOR, '.form-control')
put.send_keys(result)

browser.find_element(By.CSS_SELECTOR, 'button').click()

time.sleep(10)
browser.quit()

