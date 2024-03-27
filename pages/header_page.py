import allure
from pages.base_page import BasePage
from locators.header_page_locators import HeaderPageLocators
from locators.dzen_page_locators import DzenPageLocators

class HeaderPage(BasePage):

    logo_samokat = HeaderPageLocators.HEADER_PAGE_LOGO_SCOOTER
    logo_yandex = HeaderPageLocators.HEADER_PAGE_LOGO_YANDEX
    card_news = DzenPageLocators.DZEN_PAGE_BUTTON
    buttonOrderHeader = HeaderPageLocators.HEADER_PAGE_ORDER_BUTTON

    @allure.step('Клик на лого "Самокат')
    def click_to_samokat_logo(self):
        self.click_to_logo(self.logo_samokat)
    @allure.step('Клик на лого Яндекс и переход на страницу')
    def click_to_yandex_logo(self):
        self.click_to_logo(self.logo_yandex)
        main_window_handle = self.driver.current_window_handle
        super().switch_to_new_tab(main_window_handle)

    @allure.step('Клик на кнопку "Заказать" в хэдере')
    def click_order_button_from_header(self):
        self.click_to_element(self.buttonOrderHeader)

    @allure.step('Проверить кнопку "Заказать" внизу страницы')
    def check_element(self, locator):
        return self.get_text_from_element(locator)
