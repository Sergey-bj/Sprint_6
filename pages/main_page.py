from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage

class MainPage(BasePage):

    def button_order(self, locator):
        self.click_to_element(locator)

    def click_to_question(self, locator):
        self.find_element_with_wait(locator).click()

    def get_text_from_answer(self, locator):
        return self.get_text_from_element(locator)

    def get_answer_text(self, locator_q, locator_a, num):
        locator_q_formatted = self.format_locators(locator_q, num)
        locator_a_formatted = self.format_locators(locator_a, num)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator_q_formatted))
        self.click_to_question(locator_q_formatted)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator_a_formatted))
        return self.get_text_from_answer(locator_a_formatted)

    def scroll_to_button_order(self, locator):
        element = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
