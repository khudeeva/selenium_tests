from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

def test_new_window():
    driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://demoqa.com/browser-windows")
    
    # сохраняем текущую вкладку
    original_tab = driver.current_window_handle

    # кликаем по кнопке "New Tab" дважды
    tab_button = driver.find_element(By.ID, "tabButton")
    tab_button.click()
    tab_button.click()

    # ждем появления 3-х вкладок
    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) == 3)

    # проходим по вкладкам, кроме оригинальной
    for handle in driver.window_handles:
        if handle!=original_tab:
            driver.switch_to.window(handle)
            heading = driver.find_element(By.ID, "sampleHeading")
            assert heading.text.strip() == "This is a sample page"

    # возвращаемся в исходную вкладку
    driver.switch_to.window(original_tab)
    assert "browser-windows" in driver.current_url
    driver.quit()