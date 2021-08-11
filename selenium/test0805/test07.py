from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys                    # 键盘
from selenium.webdriver.common.action_chains import ActionChains   # 鼠标

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")

driver.find_element_by_xpath("//*[@id='kw']").send_keys("天气之子")
# 鼠标
q = driver.find_element_by_xpath("//*[@id='su']")
ActionChains(driver).double_click(q).perform()  # 双击
time.sleep(4)
q = driver.find_element_by_xpath("//*[@id='1']/h3/a")
ActionChains(driver).context_click(q).perform()  # 右击
time.sleep(4)
driver.quit()