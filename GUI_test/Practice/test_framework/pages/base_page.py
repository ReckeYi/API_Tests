class BasePage:
    def __init__(self, browser):
        self.browser = browser # Браузер внутри класса равен браузеру, который передали в класс

    def find(self, args):
        return self.browser.find_element(*args)
