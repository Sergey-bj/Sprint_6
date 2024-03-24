from pages.base_page import BasePage

class OrderPage(BasePage):

    def go_to_order_form(self, locator):
        self.find_element_with_wait(locator).click()

    def scroll_to_button_order(self, locator):
        self.scroll_to_element(locator)

    def set_order_personal(self, name_locator, name, last_name_locator, last_name, address_locator,
                           address, station_locator, station, station_select, phone_locator, phone):
        self.add_text_to_element(name_locator, name)
        self.add_text_to_element(last_name_locator, last_name)
        self.add_text_to_element(address_locator, address)
        self.find_element_with_wait(station_locator).click()
        self.add_text_to_element(station_locator, station)
        self.find_element_with_wait(station_select).click()
        self.add_text_to_element(phone_locator, phone)

    def click_button_next(self, locator):
        self.find_element_with_wait(locator).click()

    def set_order_data(self, date_locator, date, date_select, rental_locator, rental_select):
        self.find_element_with_wait(date_locator).click()
        self.add_text_to_element(date_locator, date)
        self.find_element_with_wait(date_select).click()
        self.find_element_with_wait(rental_locator).click()
        self.find_element_with_wait(rental_select).click()

    def click_button_order(self, locator):
        self.find_element_with_wait(locator).click()

    def click_button_order_yes(self, locator):
        self.find_element_with_wait(locator).click()

    def check_order(self, locator):
        return self.get_text_from_element(locator)