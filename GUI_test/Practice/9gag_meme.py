from selenium import webdriver
from selenium.webdriver.common.by import By

#open browser
driver = webdriver.Chrome()

#go to the website page
driver.get('https://9gag.com/trending')

#find by class name
first_meme = driver.find_element(By.CLASS_NAME, 'badge-evt')

#get attribute
first_meme_url = first_meme.get_attribute('href')

with open('meme.txt', 'w') as meme_file:
    meme_file.write(first_meme_url)