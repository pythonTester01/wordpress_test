from base.page_objects import PageObject,PageElement,PageElements

class topicPage(PageObject):

    title = PageElement(css=".LEFT>h1")
    #content = PageElement(id_="TopNav")

    content = PageElement(class_="content-article",time_out=3)
    def get_top_url(self):
        js = 'return $(".news-top>a")[2].getAttribute("href")'
        return self.driver.execute_script(js)


    def get_content(self):

        self.driver.find_element_by_id("TopNav").get_attribute('innerHTML')


