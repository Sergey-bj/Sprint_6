from selenium.webdriver.common.by import By

class OrderPageLocators:

    #ORDER_PERSONAL_DATA_FORM_PAGE
    ORDER_PAGE_NAME_INPUT = By.XPATH, ".//input[@class='Input_Input__1iN_Z Input_Responsible__1jDKN' and @placeholder='* Имя']"  # Поле ввода "Имя"
    ORDER_PAGE_SURNAME_INPUT = By.XPATH, ".//input[@class='Input_Input__1iN_Z Input_Responsible__1jDKN' and @placeholder='* Фамилия']" # Поле ввода "Фамилия"
    ORDER_PAGE_ADDRESS_INPUT = By.XPATH, ".//input[@class='Input_Input__1iN_Z Input_Responsible__1jDKN' and @placeholder='* Адрес: куда привезти заказ']" # Поле ввода "Адресa"

    ORDER_PAGE_METRO_STATION_CLICK = By.XPATH, ".//input[@placeholder = '* Станция метро']"   # Активировать поле
    ORDER_PAGE_METRO_STATION_SELECT = By.XPATH, ".//div[text()='Черкизовская']"   # Проверка станции
    ORDER_PAGE_METRO_STATION_SELECT_V2 = By.XPATH, ".//div[text()='Парк культуры']"    # Проверка станции

    ORDER_PAGE_PHONE_NUMBER_INPUT = By.XPATH, ".//input[@class='Input_Input__1iN_Z Input_Responsible__1jDKN' and @placeholder='* Телефон: на него позвонит курьер']" # Поле ввода "Телефона"

    #INPUT_BUTTON
    ORDER_PAGE_INPUT_BUTTON = By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Далее']" # Кнопка "Далее"

    # ORDER_SERVICE_DATA_FORM_PAGE
    ORDER_PAGE_DATE_CLICK = By.XPATH, ".//input[@placeholder = '* Когда привезти самокат']"   # Поле "* Когда привезти самокат"
    ORDER_PAGE_DATE_SELECT = By.XPATH, ".//div[@aria-label='Choose четверг, 28-е марта 2024 г.']"    # Найти элемент
    ORDER_PAGE_DATE_SELECT_V2 = By.XPATH, ".//div[@aria-label='Choose понедельник, 30-е сентября 2024 г.']"   # Найти элемент

    ORDER_PAGE_DATE_RENTAL_CLICK = By.XPATH, ".//div[@class='Dropdown-placeholder' and text()='* Срок аренды']"  # Поле Срок аренды
    ORDER_PAGE_DATE_RENTAL_SELECT = By.XPATH, ".//div[@class='Dropdown-option' and text()='сутки']"    # Найти элемент сутки
    ORDER_PAGE_DATE_RENTAL_SELECT_V2 = By.XPATH, ".//div[@class='Dropdown-option' and text()='двое суток']"  # Найти элемент двое суток

    ORDER_PAGE_GREY_CHECK_BOX = By.XPATH, "//input[@id='grey']" # Выбор чекбокс
    ORDER_PAGE_INPUT_COMMENT = By.XPATH, "//input[@placeholder='Комментарий для курьера']"

    ORDER_PAGE_DROPDOWN_CONTROL_INPUT = By.XPATH, ".//div[@class='Dropdown-placeholder' and text()='* Срок аренды']"   # Поле "Срок аренды"
    ORDER_PAGE_DROPDOWN_CONTROL = By.XPATH, ".//div[@class='Dropdown-option is-selected' and text()='сутки']"  # Выбор Срока аренды

    ORDER_PAGE_ORDER_CHECKBOXES_BLACK = By.XPATH, ".//input[@class='Checkbox_Input__14A2w' and text()='чёрный жемчуг']"    # Чекбокс "Цвет самоката"
    ORDER_PAGE_ORDER_CHECKBOXES_GREY = By.XPATH, ".//input[@class='Checkbox_Input__14A2w' and text()='серая безисходность']"   # Чекбокс "Цвет самоката"

    ORDER_PAGE_COMMENTS_INPUT = By.XPATH, ".//input[@class='Input_Input__1iN_Z Input_Responsible__1jDKN' and placholder()='Комментарий для курьера']"  # Поле ввода "Комментарий"

    # ORDER_BUTTON
    ORDER_PAGE_ORDER_BUTTON = By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']" # Кнопка "Заказать"
    ORDER_PAGE_BACK_BUTTON = By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM Button_Inverted__3IF-i' and text()='Назад']" # Кнопка "Назад"

    # AGREEMENT_MODAL_WINDOW
    ORDER_PAGE_MODAL_WINDOW_ORDER_BUTTON = By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']"  # Кнопка "Да" в модальном окне
    ORDER_PAGE_MODAL_WINDOW_BACK_BUTTON = By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM Button_Inverted__3IF-i' and text()='Нет']"  #  Кнопка "Нет" в модальном окне

    # SUCCESSFULL_MODAL_WINDOW
    ORDER_PAGE_SUCCESSFULL_MODAL_WINDOW = By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']"  # Модальное окно успешного заказа
    ORDER_PAGE_SUCCESSFULL_MODAL_WINDOW_BUTTON = By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Посмотреть статус']" # Кнопка "Посмотреть статус"


