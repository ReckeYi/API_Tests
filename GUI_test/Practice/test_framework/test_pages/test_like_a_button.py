from GUI_test.Practice.test_framework.pages.like_a_button import LikeAButtonPage

'''Исходные тесты'''


# def test_button2_exist(browser):
#     browser.get('https://www.qa-practice.com/elements/button/like_a_button')
#     assert browser.find_element(By.LINK_TEXT, 'Click').is_displayed()
#
#
# def test_button2_clicked(browser):
#     browser.get('https://www.qa-practice.com/elements/button/like_a_button')
#     browser.find_element(By.LINK_TEXT, 'Click').click()
#     assert 'Submitted' == browser.find_element(By.ID, 'result-text').text


'''Тесты с использованием фреймворка'''


def test_button2_exist(browser):
    like_a_page = LikeAButtonPage(browser)
    like_a_page.open()
    assert like_a_page.button_is_displayed


def test_button2_clicked(browser):
    like_a_button_page = LikeAButtonPage(browser)
    like_a_button_page.open()
    like_a_button_page.click_button()
    assert 'Submitted' == like_a_button_page.result_test
