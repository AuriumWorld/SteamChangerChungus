from selenium import webdriver
import time
import random

#List of names the program can choose from (CSGO Bot names)
names = ('BOT Albert', 'BOT Allen', 'BOT Bert', 'BOT Bob', 'BOT Cecil', 'BOT Clarence', 'BOT Elliot', 'BOT Elmer', 'BOT Ernie', 'BOT Eugene', 'BOT Fergus', 'BOT Ferris'
, 'BOT Frank', 'BOT Frasier', 'BOT Fred', 'BOT George', 'BOT Graham', 'BOT Harvey', 'BOT Irwin', 'BOT Larry', 'BOT Lester', 'BOT Marvin', 'BOT Neil', 'BOT Niles'
, 'BOT Oliver', 'BOT Opie', 'BOT Ryan', 'BOT Toby', 'BOT Ulric', 'BOT Ulysses', 'BOT Uri', 'BOT Waldo', 'BOT Wally', 'BOT Walt', 'BOT Wesley', 'BOT Yanni'
, 'BOT Yogi', 'BOT Yuri')
#How often the program changes your name (seconds)
name_change_time = 30

driver = webdriver.Firefox()

username = input('Enter Steam username:')
password = input('Enter Steam password:')

driver.get('https://steamcommunity.com/login/home/?goto=')
driver.find_element_by_id("input_username").send_keys(username)
driver.find_element_by_id("input_password").send_keys(password)
driver.find_element_by_class_name('login_btn').click()
print('30 seconds to enter your steam code!')
time.sleep(30)
driver.find_element_by_class_name('btn_medium').click()
time.sleep(3)

def name_change():

    current_name = random.choice(names)

    driver.find_element_by_class_name('DialogTextInputBase').clear()
    driver.find_element_by_class_name('DialogTextInputBase').send_keys(current_name)
    driver.find_element_by_xpath('/html/body/div[1]/div[7]/div[3]/div/div[2]/div/div/div[3]/div[2]/div[2]/form/div[7]/button[1]').click()
    print("Your name is now", current_name)

while True:
    name_change()
    time.sleep(name_change_time)
