import pytest
import allure
from pages.main_page import MainPage

class TestMainPage:

    @allure.title("Проверка корректного отображения текста в ответе")
    @pytest.mark.parametrize("pointer_index, expected_text", [
        (0, "Сутки — 400 рублей"),
        (1, "Пока что у нас так"),
        (2, "вы оформляете заказ на 8 мая"),
        (3, "Только начиная с завтрашнего дня"),
        (4, "Пока что нет"),
        (5, "Самокат приезжает к вам с полной зарядкой"),
        (6, "пока самокат не привезли"),
        (7, "Всем самокатов!")
    ])
    def test_click_pointer(self, driver, pointer_index, expected_text):
        main_page = MainPage(driver)
        main_page.click_button_cookie()
        main_page.scroll_to_pointer()
        main_page.click_pointer(pointer_index)
        assert expected_text in main_page.get_text_under_pointer(pointer_index)
