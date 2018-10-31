from base.page_objects import PageObject,PageElement,PageElements
from page.EditPostPage import EditPostPage
class DashboardPage(PageObject):

    greeting_link = PageElement(css="#wp-admin-bar-my-account .ab-item")
    create_posts = PageElement(css="#wp-admin-bar-new-content > a > span.ab-label")

    # wp-admin-bar-new-content > a > span.ab-label
    def create_post(self):
        self.create_posts.click()
        return EditPostPage(self.driver)
