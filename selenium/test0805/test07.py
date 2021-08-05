from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")

driver.find_element_by_xpath("//*[@id='kw']").send_keys("天气之子")
driver.find_element_by_xpath("//*[@id='su']").click()
time.sleep(4)
driver.quit()