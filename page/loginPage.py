from base.page_objects import PageObject,PageElement,PageElements
from page.DashboardPage import DashboardPage
class loginPage(PageObject):

    username = PageElement(id_="user_login")
    password = PageElement(id_="user_pass")
    login_btn = PageElement(id_="wp-submit")

    def login_success(self,input_username,input_password):
        self.username.send_keys(input_username)
        self.password.send_keys(input_password)
        self.login_btn.click()

        return DashboardPage(self.driver)


