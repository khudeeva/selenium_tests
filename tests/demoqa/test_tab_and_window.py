from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_tab_and_window():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://demoqa.com/browser-windows")

    # сохраняем текущую вкладку
    original_tab = driver.current_window_handle

    # кликаем по кнопкам "New Tab", "New Window"
    driver.find_element(By.ID, "tabButton").click()
    driver.find_element(By.ID, "windowButton").click()
    # ждем, пока вкладок\окон станет 3
    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) == 3)
    # перебираем вкладки
    for handle in driver.window_handles:
        if handle != original_tab:
            driver.switch_to.window(handle)
            heading = driver.find_element(By.ID, "sampleHeading")
            assert heading.text.strip() == "This is a sample page"
    driver.switch_to.window(original_tab)
    assert "browser-windows" in driver.current_url

    driver.quit()