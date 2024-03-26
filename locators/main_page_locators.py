from selenium.webdriver.common.by import By

class MainPageLocators:

    # #ORDER_BUTTON
    MAIN_PAGE_ORDER_BUTTON = By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']"   #  Кнопка "Заказать" внизу страницы

    # Вопросы о важном
    QUESTION0 = By.XPATH, "//div[@id='accordion__heading-0']"
    QUESTION1 = By.XPATH, "// div[ @ id = 'accordion__heading-1']"
    QUESTION2 = By.XPATH, "//div[@id='accordion__heading-2']"
    QUESTION3 = By.XPATH, "//div[@id='accordion__heading-3']"
    QUESTION4 = By.XPATH, "//div[@id='accordion__heading-4']"
    QUESTION5 = By.XPATH, "//div[@id='accordion__heading-5']"
    QUESTION6 = By.XPATH, "//div[@id='accordion__heading-6']"
    QUESTION7 = By.XPATH, "//div[@id='accordion__heading-7']"

    # Ответы
    ANSWER0 = By.XPATH, "//p[contains(text(),'Сутки — 400 рублей. Оплата курьеру — наличными или')]"
    ANSWER1 = By.XPATH,"//p[contains(text(),'Пока что у нас так: один заказ — один самокат. Есл')]"
    ANSWER2 = By.XPATH, "//p[contains(text(),'Допустим, вы оформляете заказ на 8 мая. Мы привози')]"
    ANSWER3 = By.XPATH, "//p[contains(text(),'Только начиная с завтрашнего дня. Но скоро станем ')]"
    ANSWER4 = By.XPATH, "//p[contains(text(),'Пока что нет! Но если что-то срочное — всегда можн')]"
    ANSWER5 = By.XPATH, "//p[contains(text(),'Самокат приезжает к вам с полной зарядкой. Этого х')]"
    ANSWER6 = By.XPATH, "//p[contains(text(),'Да, пока самокат не привезли. Штрафа не будет, объ')]"
    ANSWER7 = By.XPATH, "//p[contains(text(),'Да, обязательно. Всем самокатов! И Москве, и Моско')]"

    #Button_COOKIE
    MAIN_PAGE_BUTTON_COOKIE = By.ID, "rcc-confirm-button"
