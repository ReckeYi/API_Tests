import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


''' Параметризация для попарного тестирования '''


users = ['user1@mail.com', 'user2@mail.com', 'user3@mail.com']
passwords = ['password', 'asdasdasd', '1234657890']


def generate_pairs():
    pairs = []
    for user in users:
        for password in passwords:
            pairs.append(pytest.param((user, password), id=f'{user}, {password}'))
    return pairs


@pytest.mark.parametrize('creds', generate_pairs())  # <- При обычной параметризации не используется
def test_login_fail(creds):
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
