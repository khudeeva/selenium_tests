from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_demoqa_tab_windows():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://demoqa.com/browser-windows")

# сохраняем ID текущей страницы
    original_tab = driver.current_window_handle
# Нажимаем на кнопку 'New Tab'
    driver.find_element(By.ID, "tabButton").click()
# ждем открытия страницы
    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles)> 1)
# переключаемся на новую вкладку
    for handle in driver.window_handles:
        if handle != original_tab:
            driver.switch_to.window(handle)
            break
# проверяем текст на новой странице
    new_text = driver.find_element(By.ID, "sampleHeading")
    assert new_text.text.strip() == "This is a sample page"
# возвращаемся на первую страницу
    driver.switch_to.window(original_tab)
# проверяем текст на первой странице
    original_text = driver.find_element(By.ID, "tabButton")
    assert original_text.text.strip() == "New Tab"

    driver.quit()