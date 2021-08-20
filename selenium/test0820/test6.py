from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

# 弹出框中的输入框处理
driver = webdriver.Chrome()

url = "file:///D:/Program/Github/Python/selenium2html/send.html"
driver.get(url)
driver.find_element_by_tag_name("input").click()
time.sleep(3)
alert = driver.switch_to.alert
alert.send_keys("哦")
alert.accept()
time.sleep(6)
driver.quit()