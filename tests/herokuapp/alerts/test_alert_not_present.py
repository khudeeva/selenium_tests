from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

def test_alert_not_present():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# ждем появления alert(но его не будет)
    try:
        WebDriverWait(driver, 3).until(
            EC.alert_is_present()
        )
        # если вдруг alert появится-переключаемся
        alert = driver.swith_to.alert
        alert.accept()
        
        # если мы дошли до сюда - тест не прошел
        assert False, "Alert не должен был появиться"
    except TimeoutException:
        # это ожидаемое поведение
        print("Alert не появился - как и должно быть")

    driver.quit()