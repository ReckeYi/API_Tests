from selenium.webdriver.common.by import By

from GUI_test.Practice.test_framework.pages.base_page import BasePage

button_selector = (By.ID, 'submit-id-submit')
result_selector = (By.ID, 'result-text')


class SimpleButtonPage(BasePage):
    def __init__(self, browser):  # При инициализации передаем в дочерний класс браузер
        super().__init__(browser)  # Передаем браузер из дочернего(SimpleButtonPage) класса родительскому(BasePage)

    def open(self):
        self.browser.get('https://www.qa-practice.com/elements/button/simple')

    def button(self):
        return self.find(button_selector)

    def button_is_displayed(self):
        return self.button().is_displayed()

    def click_button(self):
        self.button().click()

    def result(self):
        return self.find(result_selector)

    @property
    def result_test(self):
        return self.result().text
