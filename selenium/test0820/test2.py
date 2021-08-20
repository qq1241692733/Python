from selenium import webdriver
import time

# 多次框架/窗口定位
driver = webdriver.Chrome()

url = "file:///D:/Program/Github/Python/selenium2html/frame.html"
driver.get(url)
driver.switch_to.frame("f1")   # 页面跳转到 f1
driver.switch_to.frame("f2")   # 在 f1框架中跳转到 f2
driver.find_element_by_id("kw").send_keys("你的名字")
driver.find_element_by_id("su").click()
time.sleep(6)

# 从 f2框架中不能直接跳转到 f1
# 先回到默认页面
driver.switch_to.default_content()
# 从默认页面定位到 f1
driver.switch_to.frame("f1")

driver.quit()