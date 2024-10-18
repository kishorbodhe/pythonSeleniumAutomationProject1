import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Invoking a browser and validating url change and log in into application
def test_chrome_login_verification():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()
    time.sleep(3)
    curnt_url = driver.current_url
    print(f"This is current url:{curnt_url}")
    make_appointment_button = driver.find_element(By.ID,value="btn-make-appointment")
    make_appointment_button.click()
    time.sleep(4)
    username = driver.find_element(By.ID, value="txt-username")
    passWord = driver.find_element(By.ID, value="txt-password")
    username.send_keys("John Doe")
    passWord.send_keys("ThisIsNotAPassword")
    submit = driver.find_element(By.ID,value="btn-login")
    submit.click()
    changed_url= driver.current_url
    print(f"This is changed url:{changed_url}")
    assert curnt_url is not changed_url




