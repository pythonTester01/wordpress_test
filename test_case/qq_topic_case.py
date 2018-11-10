from base.my_unit_test import MyTest
from page.topicPage import topicPage
from page.loginPage import loginPage
from page.DashboardPage import DashboardPage
from page.EditPostPage import EditPostPage
from page.PostListPage import PostListPage
from time import sleep
class login_case(MyTest):



    def test_qq_topic(self):
        '''测试腾讯今日话题'''
        page = topicPage(self.dr)
        page.get("https://www.qq.com/")

        top_url = page.get_top_url()

        page.get(top_url)
        #page.get("http://view.inews.qq.com/a/20180912A0PFDL00")

        qq_title = page.title.text
        qq_content = page.content.get_attribute('innerHTML')
        qq_content = qq_content.replace('\"','\'').replace('\n','').strip()#.replace(' ','')

        page = loginPage(self.dr)
        page.get(self.url)
        page.login_success(self.username, self.password)

        dashboardPage = DashboardPage(self.dr)
        dashboardPage.create_post()

        editPostPage = EditPostPage(self.dr)
        editPostPage.title.send_keys(qq_title)
        sleep(2)
        # #editPostPage.text_btn.click()
        sleep(2)
        #editPostPage.text_content.clear()
        #editPostPage.set_text_content(qq_content)
        editPostPage.set_content(qq_content)
        editPostPage.publish_btn.click()

        postListPage = PostListPage(self.dr)

        postListPage.get("http://139.199.192.100:8000/wp-admin/edit.php")

        new_title = postListPage.edit_page_title.text

        self.assertEqual(new_title, qq_title)
