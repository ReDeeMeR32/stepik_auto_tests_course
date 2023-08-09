import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

driver.get("https://vk.com/feed")
time.sleep(5)
press = driver.find_element(By.CSS_SELECTOR, "#l_msg button")
press.click()
time.sleep(2)
driver.quit()