from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service

def test_iframe_in_new_tab():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/windows")
# сохраняем url текущей вкладки
    original_tab = driver.current_window_handle
# кликнуть на 'Click Here'
    driver.find_element(By.LINK_TEXT, "Click Here").click()

# ждем переключения на новую вкладку
    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles)>1)

# переключаемся на новую вкладку
    for handle in driver.window_handles:
        if handle != original_tab:
            driver.switch_to.window(handle)
            break

# переходим на url вручную
    driver.get("https://the-internet.herokuapp.com/iframe")

# ждем, пока фрейм появится на странице
    WebDriverWait(driver, 10).until(
        EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, "iframe"))
    )
# очищаем и вводим текст
    editor = driver.find_element(By.ID, "tinymce")
    editor.send_keys(Keys.CONTROL + "a")
    editor.send_keys(Keys.DELETE)
    editor.send_keys("Тест в новой вкладке")

# возвращаемся на основную страницу
    driver.switch_to.default_content()

# проверим, что заголовок содержит текст
    heading = driver.find_element(By.TAG_NAME, "h3")
    assert heading.text.strip() == "An iFrame containing the TinyMCE WYSIWYG Editor"

    driver.quit()
