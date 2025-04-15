from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


def test_edit_text_in_iframe():
    # запуск браузера и открытие страницы
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/iframe")

    # ждём, пока фрейм появится на странице
    WebDriverWait(driver, 10).until(
        EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, "iframe"))
    )

    # внутри iframe: очищаем и вводим новый текст
    editor = driver.find_element(By.ID, "tinymce")
    editor.send_keys(Keys.CONTROL + "a")  # выделить весь текст
    editor.send_keys(Keys.DELETE)         # удалить
    editor.send_keys("Автотест в редакторе")


    # возвращаемся в основное содержимое страницы
    driver.switch_to.default_content()

    # проверяем, что заголовок остался прежним
    heading = driver.find_element(By.TAG_NAME, "h3")
    assert heading.text.strip() == "An iFrame containing the TinyMCE WYSIWYG Editor"

    driver.quit()
