from selenium import webdriver
import allure
import pytest
from selenium.webdriver.ie.webdriver import WebDriver


@allure.title("Verify the Title of the webpage app.vwo.com" )
def test_sample():
    driver = webdriver.Edge()
    driver.get("https://www.sdet.live.com")
    driver.title()

#Selenium 3 Not much used now a days
# driver_path = "C:/Users/USER/Downloads/edgedriver_win64"
# driver = webdriver.EdgeService(executable_path=driver_path)
# driver.get("https://www.sdet.live.com")
# assert driver.current_url == "https://www.sdet.live.com"


#

