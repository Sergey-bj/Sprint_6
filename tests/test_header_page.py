import allure
from pages.dzen_page import DzenPage
from pages.header_page import HeaderPage


@allure.story('Тест перехода по клику на лого')
class TestHeaderPage:

    @allure.title('Проверка клика на логотип "Самоката"')
    def test_click_logo_successful(self, driver):
        header_page = HeaderPage(driver)
        header_page.click_order_button_from_header()
        header_page.click_to_samokat_logo()
        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

    @allure.title('Проверка клика на логотип "Яндекс"')
    def test_click_yandex_logo(self, driver):
        header_page = HeaderPage(driver)
        header_page.click_to_yandex_logo()
        dzen_page = DzenPage(driver)
        text_from_card = dzen_page.get_elements_news()
        assert any('Новости' in item for item in text_from_card)
