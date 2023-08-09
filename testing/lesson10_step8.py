import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")


button = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element
                                          ((By.CSS_SELECTOR, "#price"), "$100"))
browser.find_element(By.CSS_SELECTOR, "#book").click()

x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
result = calc(x_element.text)

put = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".form-control")))
put.send_keys(result)


browser.find_element(By.CSS_SELECTOR, '#solve').click()
time.sleep(10)
browser.quit()
