import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


''' Простая Параметризация '''


@pytest.mark.parametrize(
    'creds',
    [
        pytest.param(
            ('user1@mail.com', 'password'),
            id='user1@mail.com, password'
        ),
        pytest.param(
            ('user2@mail.com', 'asdasdasd'),
            id='user2@mail.com, asdasdasd'
        ),
        pytest.param(
            ('user3@mail.com', '1234657890'),
            id='user3@mail.com, 1234657890'
        )
    ]
)
def test_login(creds):
    login, password = creds
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get('https://magento.softwaretestingboard.com/customer/account/login/referer'
               '/aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS8%2C/')
    driver.find_element(By.ID, 'email').send_keys(login)
    driver.find_element(By.ID, 'pass').send_keys(password)
    driver.find_element(By.ID, 'send2').click()
    error_text = driver.find_element(By.CSS_SELECTOR, '[data-ui-id="message-error"]').text
    assert (
            'The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again '
            'later.'
            == error_text)
