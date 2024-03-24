from pages.header_page import HeaderPage
from locators.header_page_locators import HeaderPageLocators
from locators.main_page_locators import MainPageLocators

class TestHeaderPage:
    def test_click_to_logo_yandex(self, driver):
        header_page = HeaderPage(driver)
        header_page.click_to_logo(HeaderPageLocators.BASE_PAGE_HEADER_LOGO_YANDEX)
        header_page.switch_to()
        assert header_page.check_element(HeaderPageLocators.DZEN_PAGE_BUTTON) == 'Новости'

    def test_click_to_logo_scooter(self, driver):
        header_page = HeaderPage(driver)
        header_page.click_header_order_button(HeaderPageLocators.BASE_PAGE_HEADER_ORDER_BUTTON)
        header_page.click_to_logo(HeaderPageLocators.BASE_PAGE_HEADER_LOGO_SCOOTER)
        assert header_page.check_element(MainPageLocators.HOME_PAGE_ORDER_BUTTON) == 'Заказать'
