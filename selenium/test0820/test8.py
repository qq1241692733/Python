from selenium import webdriver
import time

# 弹出框中的元素
driver = webdriver.Chrome()

url = "file:///D:/Program/Github/Python/selenium2html/upload.html"
driver.get(url)
time.sleep(2)
driver.find_element_by_name("file").send_keys("D:/Program/Github/Python/selenium2html/upload.html")
time.sleep(6)
driver.quit()