from selenium.webdriver.common.by import By

class HeaderPageLocators:

    # LOGO_BUTTON
    HEADER_PAGE_LOGO_YANDEX = By.XPATH, '//a[@href="//yandex.ru"]'  # Кнопка Яндекс ведет на страницу Дзэн
    HEADER_PAGE_LOGO_SCOOTER = By.XPATH, '//a[@class="Header_LogoScooter__3lsAR" and @href="/"]'  # Кнопка Самокат ведет на главную страницу

    # ORDER_BUTTON
    HEADER_PAGE_ORDER_BUTTON = By.XPATH, "//button[@class='Button_Button__ra12g' and text()='Заказать']" # Кнопка "Заказать" в шапке страницы

