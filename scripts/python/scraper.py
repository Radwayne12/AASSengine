from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

from time import sleep

from json import dump, loads

# Fix auto closing browser
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# setup
driver = webdriver.Chrome(options=options)

meta_file = open('scripts/data/meta.json', 'r')
while not meta_file:
    meta_file.close()
    meta_file = open('scripts/data/meta.json', 'r')
content = loads(meta_file.read())
target = content['url']
if target[:5] != 'https': 
    target = 'https://' + target
filetype = content['format']
location = content['option']
phrase = content['phrase']


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
    if not phrase:
        input_field.send_keys(f'site:{target} filetype:{filetype}')
    elif location == "inwebpage":
        input_field.send_keys(f'site:{target} filetype:{filetype} "{phrase}"')
    else:
        input_field.send_keys(f'site:{target} filetype:{filetype} {location}:{phrase}')
    actions.key_down(Keys.ENTER)
    actions.perform()


def get_links():
    global link_title

    link_title = dict()
    title_list = driver.find_elements(By.CLASS_NAME, 'MjjYud')

    for container in title_list:
        key = container.find_elements(By.TAG_NAME, 'a')
        if len(key) != 1:
            continue
        value = container.find_element(By.TAG_NAME, 'h3').text
        link_title[key[0].get_attribute('href')] = value
    print(link_title)
    


get_google()

sleep(1)

get_links()
print(link_title)

with open('scripts/data/scraped.json', 'w', encoding='utf-8') as file:
    dump(link_title, file, ensure_ascii=False)

sleep(1)
driver.close()
