from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_radio_button_click():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://demoqa.com/radio-button")

    # кликаем по видимой надписи Yes
    driver.find_element(By.XPATH, "//label[text()='Yes']").click()

    # ждем появления текста под кнопкой
    result = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "text-success"))
    )
    assert result.text.strip() == "Yes"
   

    driver.quit()