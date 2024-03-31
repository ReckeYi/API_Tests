import pytest
from selenium import webdriver


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