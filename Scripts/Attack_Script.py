import time
import random
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import sys

usernameStr = 'test'
passwordStr = 'test'

driver = webdriver.Chrome("/Users/alexbrown/Desktop/chromedriver");
driver.get(("https://www.fyletikesmaxes.gr/"));
    
driver.find_element_by_name("username").send_keys("test");
driver.find_element_by_name("password").send_keys("test");
driver.find_element_by_class_name("btn-login").click();
time.sleep(random.randint(2,4));
driver.find_element_by_class_name("world_button_active").click();
time.sleep(random.randint(2,4));

pyautogui.click(x=304, y=198)
time.sleep(2)
pyautogui.click(x=532, y=706)
time.sleep(2)
pyautogui.click(x=292, y=731)
time.sleep(2)
#pyautogui.click(x=453, y=525)         #scouts
pyautogui.click(x=853, y=570)           #light
time.sleep(2)
pyautogui.click(x=647, y=679)

time = driver.find_element_by_id("date_arrival").text
while time != "σήμερα στις 17:44:00":
    time = driver.find_element_by_id("date_arrival").text
pyautogui._autoPause(0.3,1)
pyautogui.click(x=453, y=492)


