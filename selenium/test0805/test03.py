from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
# driver.maximize_window()
# driver.find_element_by_id("kw").send_keys("吴亦凡")
# driver.find_element_by_id("su").click()
# time.sleep(1)
#
# # 清除文本 clear
# # driver.find_element_by_id("kw").submit()
# driver.find_element_by_id("kw").clear()
# time.sleep(1)
#
# driver.find_element_by_id("kw").send_keys("吴签")
# # submit 提交表单 和click一样
# driver.find_element_by_id("su").submit()
# time.sleep(2)
# driver.close()

# # 获得文本信息
# text = driver.find_element_by_id("bottom_layer").text
# print(text)
# time.sleep(2)
# driver.quit()

print(driver.title)
print(driver.current_url)

driver.find_element_by_id("kw").send_keys("你的名字")
driver.find_element_by_id("su").click()
# 等待加载出来
# 固定等待 sleep  智能等待 implicitly_wait()
driver.implicitly_wait(8)

driver.find_element_by_xpath("//*[@id='2']/h3/a").click()
print(driver.title)
print(driver.current_url)
time.sleep(6)
driver.quit()
