from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def test_valid_login_full_check():
    # запускаем Chrome с WebDriver Manager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # переходим на страницу логина
    driver.get("https://the-internet.herokuapp.com/login")

    # Вход с корректными данными
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    #ждем появления текста об успешном входе
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "flash"),"You logged into a secure area!")
    )
    
    # Проверка текста
    flash_message = driver.find_element(By.ID, "flash")
    assert "You logged into a secure area!" in flash_message.text.strip()

    # Ждем пока URL изменится(редирект на /secure)
    WebDriverWait(driver, 10).until(EC.url_contains("secure"))
    
    # Проверка URL
    assert "secure" in driver.current_url

    # ждем, пока кнопка Logout станет кликабельна
    logout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.button.secondary.radius"))
    )
    
    # Проверка кнопки Logout
    assert logout_button.is_displayed(), "Кнопка logout не отображается!"

    driver.quit()
