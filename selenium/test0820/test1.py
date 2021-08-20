from selenium import webdriver
import time
import os

# 定位一组元素
driver = webdriver.Chrome()

# url = "file:///" + os.path.abspath("D:/Program/Github/Python/selenium2html/checkbox.html")
file = "file:///D:/Program/Github/Python/selenium2html/checkbox.html"
driver.get(file)

inputs = driver.find_elements_by_tag_name("input")
for input in inputs:
    if input.get_attribute('type') == 'checkbox':
        input.click()
        time.sleep(1)
time.sleep(3)
driver.quit()