from base.page_objects import PageObject,PageElement,PageElements
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.support.ui import Select
class PostListPage(PageObject):
    edit_page_title = PageElement(css=".row-title")
    new_post_row = PageElement(css="a.submitdelete")

    def by_id(self,row_id):
        return PageElement(id_=row_id)

    def move_to_element(self,new_post_row):
        ActionChains(self.driver).move_to_element(new_post_row).perform()

    @property
    def set_row_id(self,post_id):
        row_id = "cb-select-" + post_id
        return PageElement(id_="%s" %(row_id))

    def move_and_delete(self,post_id):
        #cb-select-890
        r_id = "cb-select-" + post_id
        #print(row_id)
        PageElement(css="#%s"%(r_id)).click()
        s1 = Select(PageElement(name="action"))
        s1.select_by_visible_text("trash")
        PageElement(id="doaction").click()
