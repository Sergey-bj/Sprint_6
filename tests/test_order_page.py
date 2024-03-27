import allure
import pytest
from pages.order_page import OrderPage

@allure.story('Тест создания заказов')
class TestOrderPage:
    @allure.title('Проверка создания заказа через кнопку "Заказать" в хэдере')
    @pytest.mark.parametrize('name, surname, address, number, comment',
                             [('Иван', 'Иванов', 'Москва', '89997773313', 'ТЕСТ')])
    def test_create_order_from_header_button_positive(self, driver, name, surname, address, number, comment):
        order_page = OrderPage(driver)
        order_page.click_order_button_from_header()
        order_page.input_name(name)
        order_page.input_surname(surname)
        order_page.input_address(address)
        order_page.select_metro()
        order_page.enter_phone_field(number)
        order_page.click_next_button()
        order_page.select_date()
        order_page.select_period()
        order_page.click_on_grey_checkbox()
        order_page.enter_comment_field(comment)
        order_page.click_order_button()
        order_page.click_yes_in_popup()
        assert order_page.get_text_from_button_in_popup() == 'Посмотреть статус'

    @allure.title('Проверка создания заказа через кнопку "Заказать" внизу страницы')
    @pytest.mark.parametrize('name, surname, address, number, comment',
                             [('Тест', 'Тестович', 'Питер', '89661112233', 'Тестовая')])
    def test_create_order_from_down_button_positive(self, driver, name, surname, address, number, comment):
        order_page = OrderPage(driver)
        order_page.click_button_cookie()
        order_page.click_order_button_from_down_page()
        order_page.input_name(name)
        order_page.input_surname(surname)
        order_page.input_address(address)
        order_page.select_metro()
        order_page.enter_phone_field(number)
        order_page.click_next_button()
        order_page.select_date()
        order_page.select_period()
        order_page.click_on_grey_checkbox()
        order_page.enter_comment_field(comment)
        order_page.click_order_button()
        order_page.click_yes_in_popup()
        assert order_page.get_text_from_button_in_popup() == 'Посмотреть статус'