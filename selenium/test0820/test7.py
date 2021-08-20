from selenium import webdriver
import time

# 弹出框中的元素
driver = webdriver.Chrome()

url = "file:///D:/Program/Github/Python/selenium2html/modal.html"
driver.get(url)
driver.find_element_by_id("show_modal").click()
time.sleep(3)
# 定位弹出框中的元素
driver.find_element_by_id("click").click()
time.sleep(3)
# driver.find_element_by_xpath("//*[@id='myModal']/div[3]/button[1]").click()

# div 定位
div = driver.find_element_by_class_name("modal-footer")
buttons = div.find_elements_by_tag_name("button")
buttons[0].click()

time.sleep(6)
driver.quit()
