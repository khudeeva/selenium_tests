from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

def test_prompt_alert():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# нажимаем на кнопку 'Click for JS Prompt'
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[onclick='jsPrompt()']"))
    )
    driver.find_element(By.CSS_SELECTOR, "button[onclick='jsPrompt()']").click()

# вводим в alert 'Selenium' и нажимаем 'OK'
    alert = driver.switch_to.alert
    alert.send_keys("Selenium")
    alert.accept()

# проверяем, что появилось сообщение 'You entered: Selenium'
    result = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "result"))
    )
    assert result.text.strip() == "You entered: Selenium"

    driver.quit()
