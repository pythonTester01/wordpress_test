from base.page_objects import PageObject,PageElement,PageElements

class EditPostPage(PageObject):

    title = PageElement(name="post_title")
    publish_btn = PageElement(id_="publish")
    delete_btn = PageElement(css="#delete-action > a")

    def set_content(self, text):
        js = 'document.getElementById("content_ifr").contentWindow.document.body.innerHTML="%s"' % (text)
        self.driver.execute_script(js)

    def editPost(self,title,text):
        self.title.send_keys(title)
        self.set_content(text)
        self.publish_btn.click()

    def get_posts_id(self,title,text):
        self.editPost(title,text)
        url = self.driver.current_url
        return  url.split("=")[1].split("&")[0]
        #http://139.199.192.100:8000/wp-admin/post.php?post=907&action=edit
