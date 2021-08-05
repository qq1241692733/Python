from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.csdn.net/")

# 定位（全局唯一）     name定位 driver.find_element_by_name()  ...
driver.find_element_by_id("toolbar-search-input").send_keys("python")
driver.find_element_by_id("toolbar-search-button").click()

time.sleep(4)

# 关闭浏览器
driver.quit()
