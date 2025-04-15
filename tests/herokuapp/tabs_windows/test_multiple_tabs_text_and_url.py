from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service

def test_multiple_tabs_text_and_url():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/windows")
    # сохраняем url текущей вкладки
    original_tab = driver.current_window_handle
    # кликнем на 'Click Here'
    driver.find_element(By.LINK_TEXT, "Click Here").click()
    # ждем переключения на новую вкладку
    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)

    # переключаемся на новую вкладку
    for handle in driver.window_handles:
        if handle != original_tab:
            driver.switch_to.window(handle)
            break

    # проверим, что текст на странице 'New Window'
    text_new_tab = driver.find_element(By.TAG_NAME, "h3")
    assert text_new_tab.text.strip() == "New Window"

    # проверим, что текущий url заканчивается на 'new'
    assert "new" in driver.current_url

    # возвращаемся на первую вкладку
    driver.switch_to.window(original_tab)

    # проверим, что заголовок страницы содержит 'Opening a new window'
    text_original_tab = driver.find_element(By.TAG_NAME, "h3")
    assert text_original_tab.text.strip() == "Opening a new window"

    driver.quit()
    