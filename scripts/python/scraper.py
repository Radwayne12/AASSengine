from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

from time import sleep

# Fix auto closing browser
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# setup
driver = webdriver.Chrome(options=options)
query = 'http://www.sberbank.ru'
filetype = 'pdf'

actions = ActionChains(driver)

def get_google():

    driver.get('https://google.com')
    sleep(2)

    #click reject cookies
    reject_cookies = driver.find_element(By.XPATH, '//*[@id="W0wltc"]/div')
    actions.click(reject_cookies)
    actions.perform()

    sleep(2)

    #input the query
    input_field = driver.find_element(By.TAG_NAME, 'textarea')
    input_field.send_keys(f'{query} filetype:{filetype}')
    actions.key_down(Keys.ENTER)
    actions.perform()

get_google()