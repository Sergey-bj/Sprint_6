import allure
from pages.base_page import BasePage
from locators.dzen_page_locators import DzenPageLocators

class DzenPage(BasePage):

    DZEN_PAGE_BUTTON = DzenPageLocators.DZEN_PAGE_BUTTON

    @allure.step("Получение элемента со страницы Дзена")
    def get_elements_news(self):
        all_elements = self.find_elements_located(DzenPage.DZEN_PAGE_BUTTON)
        text_from_card = [element.text for element in all_elements]
        return text_from_card