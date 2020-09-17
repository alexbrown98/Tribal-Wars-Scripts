import time
import random
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import sys


def remove_brackets(text):
    new1 = text.replace('(', '');
    new = new1.replace(')', "");
    return new;

def check_available_scavenge():
    scavenges = driver.find_elements_by_class_name("status-specific");
    i = 0;
    for s in scavenges:
        if s.find_element_by_class_name("wood-value").text == '0':
            i += 1;
    return i;

def check_available_scavenge_not_unlocked():
    scavenges = driver.find_elements_by_class_name("status-specific");
    scavenges.pop();
    i = 0;
    for s in scavenges:
        if s.find_element_by_class_name("wood-value").text == '0':
            i += 1;
    return i;




def start_scavenge(troop_count) :
    scavenges = driver.find_elements_by_class_name("status-specific");
    for s in scavenges:
        if s.find_element_by_class_name("wood-value").text == '0':
            driver.find_element_by_name("spear").send_keys(troop_count);
            s.find_element_by_link_text("Έναρξη").click();
            time.sleep(3)
            troop_count = int(remove_brackets(driver.find_element_by_class_name("units-entry-all").text));
            if check_available_scavenge() > 0:
                troop_count = troop_count // check_available_scavenge();


def start_scavenge_not_unlocked(troop_count) :
    scavenges = driver.find_elements_by_class_name("status-specific");
    scavenges.pop();
    for s in scavenges:
        if s.find_element_by_class_name("wood-value").text == '0':
            driver.find_element_by_name("spear").send_keys(troop_count);
            s.find_element_by_link_text("Έναρξη").click();
            time.sleep(3);
            troop_count = int(remove_brackets(driver.find_element_by_class_name("units-entry-all").text));
            if check_available_scavenge_not_unlocked() > 0:
                troop_count = troop_count // check_available_scavenge_not_unlocked();



usernameStr = 'test'
passwordStr = 'test'


while 1 > 0:



    driver = webdriver.Chrome("/Users/alexbrown/Desktop/chromedriver");
    driver.get(("https://www.fyletikesmaxes.gr/"));

    driver.find_element_by_name("username").send_keys("test");
    driver.find_element_by_name("password").send_keys("test");
    driver.find_element_by_class_name("btn-login").click();
    time.sleep(random.randint(2,4));
    driver.find_element_by_class_name("world_button_active").click();
    time.sleep(random.randint(2,4));
    driver.get(("https://gr60.fyletikesmaxes.gr/game.php?village=1464&screen=place&mode=scavenge"));
    time.sleep(random.randint(1,2));

#village 1
    troops = driver.find_element_by_class_name("units-entry-all").text;
    num_troops = int(remove_brackets(troops));

    if num_troops < 30:
        driver.find_element_by_class_name("arrowRight").click();
        time.sleep(random.randint(2,4));
    else:
        new_troops1 = remove_brackets(troops);
        new_troops = int(new_troops1);
        i = check_available_scavenge();
        new_troops = new_troops // i;
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(random.randint(1,3));
        start_scavenge(new_troops);
        time.sleep(random.randint(2,4));
        driver.execute_script("window.scrollTo(0, -1000)")
        driver.find_element_by_class_name("arrowRight").click();
        time.sleep(random.randint(3,5));



#village 2
    troops = driver.find_element_by_class_name("units-entry-all").text;
    num_troops = int(remove_brackets(troops));

    if num_troops < 30:
        driver.find_element_by_class_name("arrowRight").click();
        time.sleep(2);
    else:
        new_troops1 = remove_brackets(troops);
        new_troops = int(new_troops1);
        i = check_available_scavenge();
        new_troops = new_troops // i;
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(random.randint(1,3));
        start_scavenge(new_troops);
        time.sleep(random.randint(2,4));
        driver.execute_script("window.scrollTo(0, -1000)")
        driver.find_element_by_class_name("arrowRight").click();
        time.sleep(random.randint(3,5));

#village 3
    troops = driver.find_element_by_class_name("units-entry-all").text;
    num_troops = int(remove_brackets(troops));

    if num_troops < 30:
        driver.find_element_by_class_name("arrowRight").click();
        time.sleep(2);
    else:
        new_troops1 = remove_brackets(troops);
        new_troops = int(new_troops1);
        i = check_available_scavenge();
        new_troops = new_troops // i;
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(random.randint(1,3));
        start_scavenge(new_troops);
        time.sleep(random.randint(2,4));
        driver.execute_script("window.scrollTo(0, -1000)")
        driver.find_element_by_class_name("arrowRight").click();
        time.sleep(random.randint(3,5));


#village 4
    troops = driver.find_element_by_class_name("units-entry-all").text;
    num_troops = int(remove_brackets(troops));

    if num_troops < 30:
        driver.find_element_by_class_name("arrowRight").click();
        time.sleep(2);
    else:
        new_troops1 = remove_brackets(troops);
        new_troops = int(new_troops1);
        i = check_available_scavenge();
        new_troops = new_troops // i;
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(random.randint(1,3));
        start_scavenge(new_troops);
        time.sleep(random.randint(2,4));
        driver.execute_script("window.scrollTo(0, -1000)")
        driver.find_element_by_class_name("arrowRight").click();
        time.sleep(random.randint(3,5));

#village 5
    troops = driver.find_element_by_class_name("units-entry-all").text;
    num_troops = int(remove_brackets(troops));

    if num_troops < 30:
        driver.find_element_by_class_name("arrowRight").click();
        time.sleep(2);
    else:
        new_troops1 = remove_brackets(troops);
        new_troops = int(new_troops1);
        i = check_available_scavenge_not_unlocked();
        new_troops = new_troops // i;
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(random.randint(1,3));
        start_scavenge_not_unlocked(new_troops);
        time.sleep(random.randint(2,4));
        driver.execute_script("window.scrollTo(0, -1000)")
        driver.find_element_by_class_name("arrowRight").click();
        time.sleep(random.randint(3,5));


    driver.close();
    time.sleep(random.randint(1000,1500));
