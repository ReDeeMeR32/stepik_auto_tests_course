import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/selects2.html")


x = browser.find_element(By.CSS_SELECTOR,"#num1")
y = browser.find_element(By.CSS_SELECTOR, "#num2")
x_text = int(x.text)
y_text = int(y.text)
sums = x_text + y_text
select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value(str(sums))

browser.find_element(By.CSS_SELECTOR, "button").click()

time.sleep(5)
browser.quit()

