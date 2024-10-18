from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_chrome_current_url_verificatiom():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
#1 - Find the Element the Anchor Tag

# Find an element given a By strategy and locator.
# 2 - We need to find the unique attribute which can find the web element
    make_appointment_element = driver.find_element(By.ID, value="btn-make-appointment")
# <a
# id="btn-make-appointment"
# href="./profile.php#login"
# class="btn btn-dark btn-lg">Make Appointment</a>

# 3 -Click on it
    make_appointment_element.click()
# 4- Verify that URL changes
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"
    time.sleep(10)
    driver.quit()
