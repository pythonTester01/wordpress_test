import unittest
from selenium import webdriver
from time import time



class MyTest(unittest.TestCase):


    def setUp(self):  # 每个用例执行之前执行
        self.url = 'http://139.199.192.100:8000/wp-login.php'
        self.dr = webdriver.Chrome()
        #self.dr = webdriver.Ie()
        self.dr.maximize_window()
        self.username = "pyse17"
        self.password = "pyse17"
        self.post_title = self.content = "selenium自动化测试脚本创建文章%s" % (time())


    def tearDown(self):
        self.dr.quit()
