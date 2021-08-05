from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("http://127.0.0.1:88/index.php")
driver.find_element_by_id("zentao").click()
driver.find_element_by_id("account").send_keys("admin")
driver.find_element_by_name("password").send_keys("jhy1241692733")
time.sleep(2)
# driver.find_element_by_id("submit").click()

# Enter 登录
time.sleep(2)
driver.find_element_by_name("password").send_keys(Keys.ENTER)
time.sleep(6)
driver.quit()
