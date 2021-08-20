from selenium import webdriver
import time
import unittest

class Baidu1(unittest.TestCase):  # ()内继承
#    测试固件
    def setUp(self):    #  def 定义方法
        self.driver = webdriver.Chrome()   #  self 全局变量
        self.url = "https://www.baidu.com/"
        # self.driver.maximize_window()
        time.sleep(3)
        # self.driver.get(self.url)
    def tearDown(self):
        self.driver.quit()
    def test_hao(self):
        driver = self.driver
        url = self.url
        driver.get(url)
        driver.find_element_by_link_text("hao123").click()
        time.sleep(6)
    if __name__ == "__main__":
        unittest.main(verbosity=0)

