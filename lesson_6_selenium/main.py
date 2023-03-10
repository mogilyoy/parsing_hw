from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import json

BASE_UPL = 'https://music.yandex.ru/chart'

service = Service('driver/chromedriver')
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.implicitly_wait(15) 
driver.get(BASE_UPL)

# close promo page
cross = driver.find_element(By.XPATH, "//div[@class='pay-promo-close-btn js-close']")
cross.click()

# scroll down to bottom
last_track = ''
while True:
    songs = driver.find_elements(By.XPATH, "//div[@class='d-track typo-track d-track_selectable d-track_with-cover d-track_with-chart']")
    actions = ActionChains(driver)
    if last_track != songs[-1]:
        actions.move_to_element(songs[-1])
        actions.perform()
        last_track = songs[-1]
    else:
        break

# parse songs
top_100 = []
for song in songs:
    track = song.find_element(By.XPATH, ".//a[@class = 'd-track__title deco-link deco-link_stronger']")
    track_url = track.get_attribute('href')
    track_name = track.text

    author = song.find_element(By.XPATH, ".//span[@class = 'd-track__artists']")
    author_url = author.find_element(By.XPATH, ".//a").get_attribute('href')
    author_name = author.find_element(By.XPATH, ".//a").text
    track_info = {
        'author': author_name,
        'author_url': author_url,
        'song_name': track_name,
        'song_url': track_url,
    }
    top_100.append(track_info)

with open('top_100.json', 'w') as f:
    json.dump(top_100, f)



