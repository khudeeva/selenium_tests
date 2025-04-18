from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_window():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://demoqa.com/browser-windows")

    # сохраняем ID текущего окна
    original_tab = driver.current_window_handle

    # находим кнопку и прокручиваем к ней
    button = driver.find_element(By.ID, "windowButton")
    driver.execute_script("arguments[0].scrollIntoView(true);", button)

    # ждем, пока кнопка станет кликабельной, и кликаем
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "windowButton")))
    button.click()

    # ждем открытия новой страницы
    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)

    # переключаемся в новое окно
    for handle in driver.window_handles:
        if handle != original_tab:
            driver.switch_to.window(handle)
            break

    # проверяем, что в новом окне есть нужный текст
    heading = driver.find_element(By.ID, "sampleHeading")
    assert heading.text.strip() == "This is a sample page"

    # возвращаемся в первое окно
    driver.switch_to.window(original_tab)

    # проверяем, что кнопка 'New Window' видна и кликабельна
    button = driver.find_element(By.ID, "windowButton")
    assert button.is_displayed() and button.is_enabled(), "Кнопка 'New Window' не доступна или не отображается"

    driver.quit()

