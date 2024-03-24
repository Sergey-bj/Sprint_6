from selenium.webdriver.common.by import By

class HeaderPageLocators:

    # BASE_PAGE
    BASE_PAGE_HEADER_LOGO_YANDEX = By.XPATH, '//a[@href="//yandex.ru"]'  # Кнопка Яндекс ведет на страницу Дзэн
    BASE_PAGE_HEADER_LOGO_SCOOTER = By.XPATH, '//a[@class="Header_LogoScooter__3lsAR" and @href="/"]'  # Кнопка Самокат ведет на главную страницу

    # ORDER_BUTTON
    BASE_PAGE_HEADER_ORDER_BUTTON = By.XPATH, "//button[@class='Button_Button__ra12g' and text()='Заказать']" # Кнопка "Заказать" в шапке

    # DZEN_PAGE
    DZEN_PAGE_BUTTON = By.XPATH, "//*[@class='floor-title__title-2v' and text()='Новости']"  # Кнопка "Новости" на страницы Дзен
