from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service

def test_switch_to_new_tab_and_back():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/windows")

# сохраняем текущий url вкладки
    original_tab = driver.current_window_handle
# кликнем по 'Click Here'
    driver.find_element(By.LINK_TEXT, "Click Here").click()
# ждем новую вкладку
    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
# переключаемся на новую вкладку
    for handle in driver.window_handles:
        if handle != original_tab:
            driver.switch_to.window(handle)
            break
# проверяем, что текст в h3 = 'New Window'
    heading = driver.find_element(By.TAG_NAME, "h3")
    assert heading.text.strip() == "New Window"
    
# возвращаемся на первую вкладку
    driver.switch_to.window(original_tab)

# проверяем, что url теперь заканчивается на 'windows'
    assert "window" in driver.current_url

    driver.quit()