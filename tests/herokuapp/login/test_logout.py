from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# войти с правильными данными, нажать logout, проверить, что снова на странице логина
def test_logout():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/login")

# вход с корреткными данными
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# ждем появления сообщения 
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "flash"))
    )
# читаем сообщение об успешном входе
    success_message = driver.find_element(By.ID, "flash")
    assert "You logged into a secure area!" in success_message.text

# нажимаем на кнопку Logout
    driver.find_element(By.CSS_SELECTOR, "a.button.secondary.radius").click()

# проверка, что вернулись на Login
    assert "login" in driver.current_url

    driver.quit()
