from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_logout_without_login():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/logout")

# проверка URL
    assert "login" in driver.current_url
    
# ожидание текста на странице
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "flash"), "You logged out of the secure area!")
    )

# проверка текста
    success_message = driver.find_element(By.ID, "flash")
    assert "You logged out of the secure area!" in success_message.text.strip()

# проверка, что кнопки Logout нет
    try:
        logout_button = driver.find_element(By.CSS_SELECTOR,"a.button.secondary.radius")
        assert not logout_button.is_displayed(), "Кнопка Logout отображается, хотя не должна!"
    except NoSuchElementException:
        pass # ОК, кнопки действия нет - всё правильно

    driver.quit()    
