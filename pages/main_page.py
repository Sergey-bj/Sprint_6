from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
import allure


@allure.suite('Проверка блока "Вопросы о важном"')
class MainPage(BasePage):

    pointer0 = MainPageLocators.QUESTION0
    pointer1 = MainPageLocators.QUESTION1
    pointer2 = MainPageLocators.QUESTION2
    pointer3 = MainPageLocators.QUESTION3
    pointer4 = MainPageLocators.QUESTION4
    pointer5 = MainPageLocators.QUESTION5
    pointer6 = MainPageLocators.QUESTION6
    pointer7 = MainPageLocators.QUESTION7
    text0 = MainPageLocators.ANSWER0
    text1 = MainPageLocators.ANSWER1
    text2 = MainPageLocators.ANSWER2
    text3 = MainPageLocators.ANSWER3
    text4 = MainPageLocators.ANSWER4
    text5 = MainPageLocators.ANSWER5
    text6 = MainPageLocators.ANSWER6
    text7 = MainPageLocators.ANSWER7
    button_cookie = MainPageLocators.MAIN_PAGE_BUTTON_COOKIE
    display_img = MainPageLocators.MAIN_PAGE_NONE_DISPLAY_ELEMENT


    @allure.step('Клик на кнопку принятия куки')
    def click_button_cookie(self):
        self.click_to_element(self.button_cookie)

    @allure.step('Скрыть картинку "Самокат"')
    def none_display_img(self):
        self.none_display(self.display_img)

    @allure.step('Скролл до стрелки')
    def scroll_to_pointer(self):
        self.scroll_into_view(self.pointer7)

    @allure.step('Клик по стрелке')
    def click_pointer(self, pointer_index):
        pointer_locator = getattr(self, f'pointer{pointer_index}')
        self.click_to_element(pointer_locator)

    @allure.step('Получить текст ответа')
    def get_text_under_pointer(self, pointer_index):
        text_locator = getattr(self, f'text{pointer_index}')
        return self.get_text_from_element(text_locator)
