from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

# 层级定位
driver = webdriver.Chrome()

url = "file:///D:/Program/Github/Python/selenium2html/drop_down.html"
driver.get(url)
time.sleep(1)
# driver.find_element_by_xpath("//*[@id='ShippingMethod']").click()

options = driver.find_elements_by_tag_name("option")
# for option in  options:
#     if option.get_attribute('value') == "10.69":
#         option.click()
options[2].click()

time.sleep(6)
driver.quit()
