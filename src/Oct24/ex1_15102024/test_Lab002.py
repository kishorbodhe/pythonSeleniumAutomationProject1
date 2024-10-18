from selenium import webdriver

def test_open_vwo_login():
    driver = webdriver.Chrome()
# post request to create a new fresh copy of chrome
# Fresh - Chrome - Session ID-

    driver.get("https://app.vwo.com")

# Code -> HTTP Request -->.ChromeDriver(Selenium Manager) -> chrome (SessionID)

    print(driver.title) #GET Request t
    assert driver.title == "Login - VWO"
