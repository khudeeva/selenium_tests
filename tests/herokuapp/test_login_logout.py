from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_login_logout():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/login")

    # вход с корректными данными
    driver.find_element(By.ID,"username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # ждем появления текста
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "flash"), "You logged into a secure area!")
    )

    # читаем текст
    success_message = driver.find_element(By.ID, "flash")
    assert "You logged into a secure area!" in success_message.text.strip()

    # выход, нажатие на Logout
    driver.find_element(By.CSS_SELECTOR, "a.button.secondary.radius").click()

    # ждем редирект
    WebDriverWait(driver, 10).until(
        EC.url_contains("login")
    )

    # проверяем URL: /login
    assert "login" in driver.current_url, "После выхода не перешли на /login"
   
    driver.quit()