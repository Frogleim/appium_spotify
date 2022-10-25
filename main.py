from appium import webdriver
from selenium.webdriver.common.by import By
import time
from multiprocessing import Process


def start_streaming(apps_names, users_data):
    for sdk_name in apps_names:

        desired_capabilities = {
            'platformName': 'Android',
            'platformVersion': '11',
            'deviceName': sdk_name,
            'app': 'C:/Users/GSD Beast N10/Desktop/Projects/Appium/spotify-8-7-72-546.apk'
        }

        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_capabilities)

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@text="Log in"]').click()
        time.sleep(2)
        driver.back()
        time.sleep(1)
        for data in users_data:

            username = driver.find_element(By.ID, 'username_text')
            username.click()
            time.sleep(1)

            email = data['email']
            username.send_keys(email)

            time.sleep(1)

            password = driver.find_element(By.ID, 'password_text')
            password.click()
            time.sleep(1)

            passwords = data['password']
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
            play = data['playlist']
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


