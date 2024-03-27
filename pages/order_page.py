from pages.base_page import BasePage
import allure
from locators.header_page_locators import HeaderPageLocators
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators

@allure.suite('Проверка оформления заказа самоката')
class OrderPage(BasePage):

    buttonOrderHeader = HeaderPageLocators.HEADER_PAGE_ORDER_BUTTON
    buttonOrderDownPage = MainPageLocators.MAIN_PAGE_ORDER_BUTTON
    inputName = OrderPageLocators.ORDER_PAGE_NAME_INPUT
    inputSurname = OrderPageLocators.ORDER_PAGE_SURNAME_INPUT
    inputAdress = OrderPageLocators.ORDER_PAGE_ADDRESS_INPUT
    chooseStation = OrderPageLocators.ORDER_PAGE_METRO_STATION_CLICK
    inputNumber = OrderPageLocators.ORDER_PAGE_PHONE_NUMBER_INPUT
    buttonNext = OrderPageLocators.ORDER_PAGE_INPUT_BUTTON
    inputWhere = OrderPageLocators.ORDER_PAGE_DATE_CLICK
    chooseCalendar = OrderPageLocators.ORDER_PAGE_DATE_SELECT
    inputPeriod = OrderPageLocators.ORDER_PAGE_DATE_RENTAL_CLICK
    choosePeriod = OrderPageLocators.ORDER_PAGE_DATE_RENTAL_SELECT
    checkBoxGrey = OrderPageLocators.ORDER_PAGE_GREY_CHECK_BOX
    inputComment = OrderPageLocators.ORDER_PAGE_INPUT_COMMENT
    buttonOrder = OrderPageLocators.ORDER_PAGE_ORDER_BUTTON
    buttonYes = OrderPageLocators.ORDER_PAGE_MODAL_WINDOW_ORDER_BUTTON
    button_check_status = OrderPageLocators.ORDER_PAGE_SUCCESSFULL_MODAL_WINDOW_BUTTON
    metroCherkizovskay = OrderPageLocators.ORDER_PAGE_METRO_STATION_SELECT
    metroParkCultury = OrderPageLocators.ORDER_PAGE_METRO_STATION_SELECT_V2
    choose28September = OrderPageLocators.ORDER_PAGE_DATE_SELECT
    choose30September = OrderPageLocators.ORDER_PAGE_DATE_SELECT_V2
    choose1days = OrderPageLocators.ORDER_PAGE_DATE_RENTAL_SELECT
    choose2days = OrderPageLocators.ORDER_PAGE_DATE_RENTAL_SELECT_V2
    button_cookie = MainPageLocators.MAIN_PAGE_BUTTON_COOKIE


    @allure.step('Клик на кнопку "Заказать" в хэдере')
    def click_order_button_from_header(self):
         self.click_to_element(self.buttonOrderHeader)

    @allure.step('Клик на кнопку "Заказать" в нижней части страницы')
    def click_order_button_from_down_page(self):
        self.click_to_element(self.buttonOrderDownPage)

    @allure.step('Ввод имени')
    def input_name(self, name):
        self.add_text_to_element(self.inputName, name)

    @allure.step('Ввод фамилии')
    def input_surname(self, surname):
        self.add_text_to_element(self.inputSurname, surname)

    @allure.step('Ввод адреса')
    def input_address(self, address):
        self.add_text_to_element(self.inputAdress, address)

    @allure.step('Выбор метро')
    def select_metro(self):
        self.choose_option_from_dropdown(self.chooseStation, self.metroCherkizovskay)

    @allure.step('Ввод номера телефона')
    def enter_phone_field(self, number):
        self.add_text_to_element(self.inputNumber, number)

    @allure.step('Клик на кнопку "Далее"')
    def click_next_button(self):
        self.click_to_element(self.buttonNext)

    @allure.step('Выбор дня')
    def select_date(self):
        self.choose_option_from_dropdown(self.inputWhere, self.chooseCalendar)

    @allure.step('Выбор периода')
    def select_period(self):
        self.choose_option_from_dropdown(self.inputPeriod, self.choose1days)

    @allure.step('Клик на чекбокс "Серый"')
    def click_on_grey_checkbox(self):
        self.click_to_element(self.checkBoxGrey)

    @allure.step('Добавить комментарий')
    def enter_comment_field(self, comment):
        self.add_text_to_element(self.inputComment, comment)

    @allure.step('Клик на кнопку "Заказать"')
    def click_order_button(self):
        self.click_to_element(self.buttonOrder)

    @allure.step('Клик на кнопку "Да"')
    def click_yes_in_popup(self):
        self.click_to_element(self.buttonYes)

    @allure.step('Получение текста из элемента')
    def get_text_from_button_in_popup(self):
        return self.get_text_from_element(self.button_check_status)

    @allure.step('Клик на кнопку "Принять куки"')
    def click_button_cookie(self):
        self.click_to_element(self.button_cookie)
