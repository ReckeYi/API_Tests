import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


''' Indirect Parametrization - Непрямая параметризация'''
''' Может использоваться для тестирования данных из БД'''


@pytest.fixture()
def page(request):  # Может быть, только параметр "request", с другими параметрами не работает
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    param = request.param
    if param == 'whats_new':
        driver.get('https://magento.softwaretestingboard.com/what-is-new.html')
    elif param == 'sale':
        driver.get('https://magento.softwaretestingboard.com/sale.html')
    return driver


@pytest.mark.parametrize('page', ['whats_new'], indirect=True)
def test_whats_new(page):
    title = page.find_element(By.CSS_SELECTOR, 'h1')
    assert title.text == 'What\'s New'


@pytest.mark.parametrize('page', ['sale'], indirect=True)
def test_sale(page):
    title = page.find_element(By.CSS_SELECTOR, 'h1')
    assert title.text == 'Sale'
