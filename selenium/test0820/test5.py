from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

# 弹出框处理
driver = webdriver.Chrome()

url = "file:///D:/Program/Github/Python/selenium2html/alert.html#"
driver.get(url)
driver.find_element_by_id("tooltip").click()
time.sleep(3)
alert = driver.switch_to.alert    # 获取弹出库
alert.accept()   # 关闭弹框
time.sleep(4)
driver.quit()