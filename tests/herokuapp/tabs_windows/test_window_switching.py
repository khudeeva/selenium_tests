from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_window_switching():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/windows")

# сохраним текущую вкладку
    original_tab = driver.current_window_handle
# нажмем на кнопку 'Click Here'
    driver.find_element(By.LINK_TEXT, "Click Here").click()
# ждем загрузки страницы
    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles)> 1)
# переключаемся на новую вкладку
    for handle in driver.window_handles:
        if handle != original_tab:
            driver.switch_to.window(handle)
            break
# проверяем появление текста
    header = driver.find_element(By.TAG_NAME, "h3")
    assert header.text.strip() == "New Window"
# возвращаемся на первую страницу
    driver.switch_to.window(original_tab)
# проверяем текст на первой странице
    original_text = driver.find_element(By.TAG_NAME, "h3")
    assert original_text.text.strip() == "Opening a new window"

    driver.quit()
