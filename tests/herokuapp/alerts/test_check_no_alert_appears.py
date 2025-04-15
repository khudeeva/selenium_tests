from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

def test_check_no_alert_appears():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    try:
    # не нажимаем ни на одну кнопку, ждем alert
        WebDriverWait(driver, 3).until(
         EC.alert_is_present()
        )
        alert = driver.switch_to.alert
        alert.accept()
        assert False, "Alert появился, хотя не должен был"
    except TimeoutException:
        print("Alert не появился - всё ОК")
    
    driver.quit()