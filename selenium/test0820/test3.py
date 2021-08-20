from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

# 层级定位
driver = webdriver.Chrome()

url = "file:///D:/Program/Github/Python/selenium2html/level_locate.html"
driver.get(url)
driver.find_element_by_link_text("Link1").click()
a = driver.find_element_by_link_text("Another action")
ActionChains(driver).move_to_element(a).perform()
time.sleep(6)
driver.quit()