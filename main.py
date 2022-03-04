# ==+==+==+== Refresh When Bot Test Comes Up ==+==+==+==

from time import sleep
import keyboard as k
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pynput.keyboard import Controller

timeBetweenLetters = 0.01 # minimum is 0.0078

keyboard = Controller()

url = "https://play.typeracer.com/"
driver = webdriver.Chrome(ChromeDriverManager().install())

print("\nBot Will Start When Game Starts\n")\

driver.get(url)

running = True # / to quit
while running:
    if k.is_pressed("/"):
        driver.quit()
        exit()
    
    # Get text to write
    text = None
    while text is None:
        if k.is_pressed("/"):
            driver.quit()
            exit()
        
        try:
            text = driver.find_element_by_xpath('//*[@id="gwt-uid-20"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div').text
        except:
            pass

    sleep(1)

    # Wait until player can type
    waitingForGo = 1
    while waitingForGo != 0:
        if k.is_pressed("/"):
            driver.quit()
            exit()
        
        try:
            waitingForGo = len(driver.find_elements_by_xpath('/html/body/div[5]/div/table/tbody/tr/td/table/tbody/tr/td[1]/img'))
        except:
            pass

    # Types Letters
    for letter in text:
        if k.is_pressed("/"):
            driver.quit()
            exit()
        
        sleep(timeBetweenLetters)
        keyboard.type(letter)