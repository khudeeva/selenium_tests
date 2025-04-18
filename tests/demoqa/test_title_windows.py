from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_title_window():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://demoqa.com/browser-windows")

# сохраняем ID текущей страницы
    original_tab = driver.current_window_handle
# Нажимаем на кнопку 'New Window'
    driver.find_element(By.ID, "windowButton").click()
# ждем переключения на новое окно
    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles)>1)
# переключаемся в новое окно
    for handle in driver.window_handles:
        if handle != original_tab:
            driver.switch_to.window(handle)
            break
# проверяем, что в новом окне есть нужный текст в заголовке
    heading = driver.find_element(By.ID, "sampleHeading")
    assert heading.text.strip() == "This is a sample page"
# возвращаемся на первую вкладку
    driver.switch_to.window(original_tab)
# проверить, что первая вкладка доступна и содержит нужный текст
    button = driver.find_element(By.ID, "windowButton")
    assert button.is_displayed() and button.is_enabled(), "Кнопка New Window недоступна или не кликабельна"
    driver.quit()