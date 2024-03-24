from pages.base_page import BasePage

class HeaderPage(BasePage):

    def click_to_logo(self, locator):
        self.find_element_with_wait(locator).click()

    def check_go_to_new_tab(self, locator):
        self.find_element_with_wait(locator).click()

    def click_header_order_button(self, locator):
        self.find_element_with_wait(locator).click()

    def check_go_to_main_page(self, locator):
        return self.find_element_with_wait(locator)

    def check_element(self, locator):
        return self.get_text_from_element(locator)


