import unittest
from selenium import webdriver
from time import sleep
from base.my_unit_test import MyTest
from page.loginPage import loginPage
from page.DashboardPage import DashboardPage
class login_case(MyTest):



    def test_login_success(self):
        '''测试登录成功'''
        page = loginPage(self.dr)
        page.get(self.url)
        page.username.send_keys(self.username)
        page.password.send_keys(self.password)
        page.login_btn.click()

        dashboard = DashboardPage(self.dr)
        greeting_link = dashboard.greeting_link.text

        #断言 是否包含pyse17
        self.assertIn(self.username,greeting_link )

        address = self.dr.current_url
        #断言 浏览器地址栏 是否包含 wp-admin
        self.assertIn("wp-admin",address)
