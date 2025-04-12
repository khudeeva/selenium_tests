from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

def test_new_tab_url_check():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/windows")

# сохраняем ID текущей страницы
    original_tab = driver.current_window_handle

# нажимаем на 'Click Here'
    driver.find_element(By.LINK_TEXT, "Click Here").click()
  
# ждем новую вкладку
    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)

# переключаемся на новую вкладку
    for handle in driver.window_handles:
        if handle != original_tab:
            driver.switch_to.window(handle)
            break
# проверяем, что url заканчивается на /windows/new
    assert "new" in driver.current_url

# возвращаемся на первую вкладку
    driver.switch_to.window(original_tab)

# проверяем что url теперь заканчивается на /windows
    assert "windows" in driver.current_url

    driver.quit()