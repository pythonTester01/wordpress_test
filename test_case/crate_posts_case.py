import unittest
from base.my_unit_test import MyTest
from page.loginPage import loginPage
from page.DashboardPage import DashboardPage
from page.EditPostPage import EditPostPage
from page.PostListPage import PostListPage

class crate_posts(MyTest):



    def test_create_post(self):
        '''测试创建文章'''
        page = loginPage(self.dr)
        page.get(self.url)
        page.login_success(self.username,self.password)

        dashboardPage = DashboardPage(self.dr)
        dashboardPage.create_post()

        editPostPage = EditPostPage(self.dr)
        editPostPage.title.send_keys(self.post_title)
        editPostPage.set_content(self.content)
        editPostPage.publish_btn.click()

        postListPage = PostListPage(self.dr)

        postListPage.get("http://139.199.192.100:8000/wp-admin/edit.php")

        new_title = postListPage.edit_page_title.text

        self.assertEqual(new_title , self.post_title)


