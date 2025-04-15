from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_checkboxes():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/checkboxes")

    # ищем все чекбоксы
    checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
    checkbox1 = checkboxes[0]
    checkbox2 = checkboxes [1]

    # проверяем, что 1й чекбокс не выбран, кликнем на него
    if not checkbox1.is_selected():
        checkbox1.click()
    assert checkbox1.is_selected()

    # проверяем, что 2й чекбокс уже выбран
    assert checkbox2.is_selected()

    driver.quit()