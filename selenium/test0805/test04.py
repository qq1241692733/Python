from selenium import webdriver
import time

# 浏览器 大小

driver = webdriver.Chrome()
# 最大化 driver.maximize_window()

driver.get("https://www.baidu.com/")
driver.set_window_size(720, 480)     # 浏览器大小
driver.find_element_by_xpath("//*[@id='kw']").send_keys("天气之子")
driver.find_element_by_xpath("//*[@id='su']").click()
time.sleep(2)

js = "var q=document.documentElement.scrollTop=10000"  # 滚动条最底端
driver.execute_script(js)
time.sleep(2)
js = "var q=document.documentElement.scrollTop=100"  # 滚动条距离顶端100
driver.execute_script(js)

time.sleep(3)
driver.back()     # 后退
time.sleep(3)
driver.forward()   # 前进
time.sleep(3)
driver.quit()