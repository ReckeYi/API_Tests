from GUI_test.Practice.test_framework.pages.simple_buttom import SimpleButtonPage


'''Исходные тесты'''


# def test_button1_exist(browser):
#     browser.get('https://www.qa-practice.com/elements/button/simple')
#     assert browser.find_element(By.ID, 'submit-id-submit').is_displayed()
#
#
# def test_button1_clicked(browser):
#     browser.get('https://www.qa-practice.com/elements/button/simple')
#     browser.find_element(By.ID, 'submit-id-submit').click()
#     assert 'Submitted' == browser.find_element(By.ID, 'result-text').text


'''Тесты с использованием фреймворка'''

def test_button1_exist(browser):
    simple_page = SimpleButtonPage(browser)
    simple_page.open()
    assert simple_page.button_is_displayed()


def test_button1_clicked(browser):
    simple_page = SimpleButtonPage(browser)
    simple_page.open()
    simple_page.click_button()
    # assert 'Submitted' == simple_page.result_test()
    '''Можно обращаться  к методу класса SimpleButtonPage как к переменной,
    если в методе класса использовать декоратор @property'''
    assert 'Submitted' == simple_page.result_test
