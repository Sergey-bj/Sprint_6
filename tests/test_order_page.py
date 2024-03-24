from pages.order_page import OrderPage
from locators.order_page_locators import OrderPageLocators
from locators.main_page_locators import MainPageLocators
from locators.header_page_locators import HeaderPageLocators

class TestOrderPage:

    def test_check_order_successfull_v1(self, driver):

        name = 'Сергей'
        lastname = 'Петров'
        address = 'Москва'
        station = 'Черкизовская'
        phone = '89998887766'
        date = '28.09.2024'

        order_page = OrderPage(driver)
        order_page.go_to_order_form(HeaderPageLocators.BASE_PAGE_HEADER_ORDER_BUTTON)
        order_page.set_order_personal(OrderPageLocators.ORDER_PAGE_NAME_INPUT, name,
                                      OrderPageLocators.ORDER_PAGE_SURNAME_INPUT, lastname,
                                      OrderPageLocators.ORDER_PAGE_ADDRESS_INPUT, address,
                                      OrderPageLocators.ORDER_PAGE_METRO_STATION_CLICK, station,
                                      OrderPageLocators.ORDER_PAGE_METRO_STATION_SELECT,
                                      OrderPageLocators.ORDER_PAGE_PHONE_NUMBER_INPUT, phone)
        order_page.click_button_next(OrderPageLocators.ORDER_PAGE_INPUT_BUTTON)
        order_page.set_order_data(OrderPageLocators.ORDER_PAGE_DATE_CLICK, date,
                                  OrderPageLocators.ORDER_PAGE_DATE_SELECT,
                                  OrderPageLocators.ORDER_PAGE_DATE_RENTAL_CLICK,
                                  OrderPageLocators.ORDER_PAGE_DATE_RENTAL_SELECT)
        order_page.click_button_order(OrderPageLocators.ORDER_PAGE_ORDER_BUTTON)
        order_page.click_button_order_yes(OrderPageLocators.ORDER_PAGE_MODAL_WINDOW_ORDER_BUTTON)
        assert order_page.check_order(OrderPageLocators.ORDER_PAGE_SUCCESSFULL_MODAL_WINDOW_BUTTON) == 'Посмотреть статус'

    def test_check_order_successfull_v2(self, driver):

        name = 'Иван'
        lastname = 'Тестов'
        address = 'Пушкино'
        station = 'Парк культуры'
        phone = '89998882211'
        date = '30.09.2024'

        order_page = OrderPage(driver)
        order_page.scroll_to_button_order(MainPageLocators.HOME_PAGE_ORDER_BUTTON)
        order_page.set_order_personal(OrderPageLocators.ORDER_PAGE_NAME_INPUT, name,
                                      OrderPageLocators.ORDER_PAGE_SURNAME_INPUT, lastname,
                                      OrderPageLocators.ORDER_PAGE_ADDRESS_INPUT, address,
                                      OrderPageLocators.ORDER_PAGE_METRO_STATION_CLICK, station,
                                      OrderPageLocators.ORDER_PAGE_METRO_STATION_SELECT_V2,
                                      OrderPageLocators.ORDER_PAGE_PHONE_NUMBER_INPUT, phone)
        order_page.click_button_next(OrderPageLocators.ORDER_PAGE_INPUT_BUTTON)
        order_page.set_order_data(OrderPageLocators.ORDER_PAGE_DATE_CLICK, date,
                                  OrderPageLocators.ORDER_PAGE_DATE_SELECT_V2,
                                  OrderPageLocators.ORDER_PAGE_DATE_RENTAL_CLICK,
                                  OrderPageLocators.ORDER_PAGE_DATE_RENTAL_SELECT_V2)
        order_page.click_button_order(OrderPageLocators.ORDER_PAGE_ORDER_BUTTON)
        order_page.click_button_order_yes(OrderPageLocators.ORDER_PAGE_MODAL_WINDOW_ORDER_BUTTON)
        assert order_page.check_order(OrderPageLocators.ORDER_PAGE_SUCCESSFULL_MODAL_WINDOW_BUTTON) == 'Посмотреть статус'