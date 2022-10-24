from appium import webdriver
from selenium.webdriver.common.by import By
import time

desired_capabilities = {
    'platformName': 'Android',
    'platformVersion': '11',
    'deviceName': 'pixel_5_-_api_30',
    'app': 'C:/Users/GSD Beast N10/Desktop/Projects/Appium/spotify-8-7-72-546.apk'
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_capabilities)

time.sleep(3)

driver.find_element(By.XPATH, '//*[@text="Log in"]').click()
time.sleep(2)

driver.back()
time.sleep(1)
username = driver.find_element(By.ID, 'username_text')
username.click()
time.sleep(1)

email = 'robertbrownlee135@gmail.com'
username.send_keys(email)

time.sleep(1)

password = driver.find_element(By.ID, 'password_text')
password.click()
time.sleep(1)

passwords = '077108803Gb'
password.send_keys(passwords)
time.sleep(1)

driver.find_element(By.ID, 'login_button').click()

time.sleep(4)
driver.find_element(By.ID, 'search_tab').click()

time.sleep(2)
# find playlist
search = driver.find_element(By.ID, 'find_search_field_text')
search.click()
time.sleep(1)
play = 'MY GEMS'
search_input = driver.find_element(By.ID, 'query')
time.sleep(1)
search_input.click()
search_input.send_keys(play)


driver.find_element(By.ID, 'row_root').click()

# play
time.sleep(1)
driver.find_element(By.ID, 'button_play_and_pause').click()

# like
time.sleep(1)
driver.find_element(By.ID, 'heart_button').click()

# # return and sign out
# time.sleep(1)
# driver.find_element(By.ID, 'your_library_tab').click()
#
# # sign out
# time.sleep(1)
# driver.find_element(By.ID, 'accessory_start').click()
#
# time.sleep(1)
# driver.swipe(470, 1800, 470, 200, 400)
