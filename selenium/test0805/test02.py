from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
# link test链接
# driver.find_element_by_link_text("直播").click()

# 部分链接
# driver.find_element_by_partial_link_text("直").click()

# xpath 唯一
driver.find_element_by_xpath("//*[@id='kw']").send_keys("天气之子")
driver.find_element_by_xpath("//*[@id='su']").click()
time.sleep(4)
driver.quit()

