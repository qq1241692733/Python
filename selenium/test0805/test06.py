from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")

driver.find_element_by_xpath("//*[@id='kw']").send_keys("天气之子")
driver.find_element_by_xpath("//*[@id='su']").click()
time.sleep(4)

# 组合键
driver.find_element_by_xpath("//*[@id='kw']").send_keys(Keys.CONTROL, 'a')
time.sleep(3)
driver.find_element_by_xpath("//*[@id='kw']").send_keys(Keys.CONTROL, 'x')
time.sleep(3)
driver.quit()

