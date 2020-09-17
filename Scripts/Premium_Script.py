import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from playsound import playsound


usernameStr = 'alexesl17'
passwordStr = 'nicole0103'

driver = webdriver.Chrome("/Users/alexbrown/Desktop/chromedriver");
driver.get(("https://www.fyletikesmaxes.gr/"));

driver.find_element_by_name("username").send_keys("alexesl17");
driver.find_element_by_name("password").send_keys("nicole0103");
driver.find_element_by_class_name("btn-login").click();
time.sleep(2);
driver.find_element_by_class_name("world_button_active").click();
time.sleep(2);
driver.get(("https://gr60.fyletikesmaxes.gr/game.php?village=1464&screen=market&mode=exchange"));
time.sleep(1);
playsound('sound.wav')





while 1 > 0:
    w = driver.find_element_by_id("premium_exchange_rate_wood").text;
    wood_price = int(w[:-3]);

    s = driver.find_element_by_id("premium_exchange_rate_stone").text;
    stone_price = int(s[:-3]);

    i = driver.find_element_by_id("premium_exchange_rate_iron").text;
    iron_price = int(i[:-3]);

    
    if wood_price < 500:
        playsound('sound.wav')

    
    if stone_price < 500:
        playsound('sound.wav')


    
    if iron_price < 500:
        playsound('sound.wav')
    print(wood_price)
    print(stone_price)
    print(iron_price)
    print ('----')



    

    time.sleep(10);

