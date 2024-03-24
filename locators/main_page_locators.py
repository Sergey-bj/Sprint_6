from selenium.webdriver.common.by import By

class MainPageLocators:

    # ACCORDION
    QUESTION_LOCATOR = By.XPATH, '//*[@id="accordion__heading-{}"]'    # Поле Вопрос
    ANSWER_LOCATOR = By.XPATH, '//*[@id="accordion__panel-{}"]'       # Поле Ответ

    #ORDER_BUTTON
    HOME_PAGE_ORDER_BUTTON = By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']"   #  Кнопка "Заказать" внизу страницы

    # ORDER_BUTTON
    HOME_PAGE_SCROLL_ELEMENT = By.XPATH, '//*[@id="accordion__heading-0"]'    # Элемент для скролла страницы
