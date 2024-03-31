import pytest
from selenium.webdriver.common.by import By

''' Indirect Parametrization - Непрямая параметризация'''
''' Может использоваться для тестирования данных из БД'''


@pytest.mark.parametrize('page', ['whats_new'], indirect=True)
def test_whats_new(page):
    title = page.find_element(By.CSS_SELECTOR, 'h1')
    assert title.text == 'What\'s New'


@pytest.mark.parametrize('page', ['sale'], indirect=True)
def test_sale(page):
    title = page.find_element(By.CSS_SELECTOR, 'h1')
    assert title.text == 'Sale'
