from base.my_unit_test import MyTest
from selenium import webdriver
from time import sleep,time
from page.loginPage import loginPage
from page.DashboardPage import DashboardPage
from page.EditPostPage import EditPostPage
from page.PostListPage import PostListPage
from selenium.common.exceptions import NoSuchElementException



class delete_posts_case(MyTest):

    def test_delete_post(self):
        '''测试创建文章'''
        page = loginPage(self.dr)
        page.get(self.url)
        page.login_success(self.username,self.password)

        dashboardPage = DashboardPage(self.dr)
        dashboardPage.create_post()

        editPostPage = EditPostPage(self.dr)
        post_id = editPostPage.get_posts_id(self.post_title,self.content)

        postListPage = PostListPage(self.dr)

        postListPage.get("http://139.199.192.100:8000/wp-admin/edit.php")

        postListPage.edit_page_title.click()

        new_title = editPostPage.title.text

        editPostPage.delete_btn.click()

        now_title = postListPage.edit_page_title.text

        self.assertNotEqual(new_title,now_title)
        #postListPage.set_row_id.click(post_id)
        #postListPage.move_and_delete(post_id)

        # with self.assertRaises(NoSuchElementException):
        #     postListPage.







