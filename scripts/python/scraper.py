from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

from time import sleep

from json import dump

# Fix auto closing browser
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# setup
driver = webdriver.Chrome(options=options)
target = 'www.sberbank.ru'
if target[:5] != 'https': 
    target = 'https://' + target
filetype = 'pdf'
location = 'intitle'
phrase = 'Акции'


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
        input_field.send_keys(f'{target} filetype:{filetype}')
    elif location == "inwebpage":
        input_field.send_keys(f'{target} filetype:{filetype} "{phrase}"')
    else:
        input_field.send_keys(f'{target} filetype:{filetype} {location}:{phrase}')
    actions.key_down(Keys.ENTER)
    actions.perform()


def get_links():
    global link_title

    # # get serps non-empy titles
    # title_list = list()
    # title_list = driver.find_elements(By.TAG_NAME, 'h3')
    # title_list = [title.text for title in title_list if title.text]
    # print(title_list, len(title_list))

    # #get links 

    # links = driver.find_elements(By.TAG_NAME,'a')
    # links_list = []
    # for link in links:
    #     if link.get_attribute('jsname') == 'UWckNb' and link.get_attribute('href')[-4:] == f'{filetype}':
    #         print(link.get_attribute('href')[-4:])
    #         links_list.append(link.get_attribute('href'))
    # print(links_list, len(links_list))

    # link_title = {links_list[i]: title_list[i] for i in range(len(title_list))}
    # print(link_title)
    # '(By.xpath("./child::*"))'
    link_title = dict()
    title_list = driver.find_elements(By.CLASS_NAME, 'MjjYud')
    # key = title_list[0].find_elements(By.TAG_NAME, 'a')
    # print(key[0].get_attribute('href'), len(key))
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

with open('scripts/data/scraped.json', 'w') as file:
    dump(link_title, file)