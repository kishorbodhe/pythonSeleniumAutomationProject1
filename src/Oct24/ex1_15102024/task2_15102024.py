from selenium import webdriver
def test_title_current_url():
    driver = webdriver.Chrome()

    driver.get("https://katalon-demo-cura.herokuapp.com/")
    print(driver.title)
    Expected_Title = "CURA Healthcare Service"
    assert driver.title == Expected_Title

    

