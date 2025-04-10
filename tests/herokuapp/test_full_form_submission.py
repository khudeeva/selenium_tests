from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

def test_full_form_submission():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://testpages.herokuapp.com/styled/basic-html-form-test.html")

    # Вводим username и password
    driver.find_element(By.NAME, "username").send_keys("autotester")
    driver.find_element(By.NAME, "password").send_keys("12345")

    # Очищаем и заполняем textarea
    textarea = driver.find_element(By.NAME, "comments")
    textarea.clear()
    textarea.send_keys("Это автотест")

    # Выбираем чекбоксы 1 и 3
    checkbox1 = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox'][value='cb1']")
    checkbox3 = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox'][value='cb3']")
    if not checkbox1.is_selected():
        checkbox1.click()
    if not checkbox3.is_selected():
        checkbox3.click()

    # Выбираем Radio 2
    radio = driver.find_element(By.CSS_SELECTOR, "input[name='radioval'][value='rd2']")
    radio.click()

    # Выбираем Drop Down Item 4
    dropdown = Select(driver.find_element(By.NAME, "dropdown"))
    dropdown.select_by_value("dd4")

    # Нажимаем Submit
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='submit'][name='submitbutton']"))
    )
    driver.find_element(By.CSS_SELECTOR, "input[type='submit'][name='submitbutton']").click()

    # Ждём редирект
    WebDriverWait(driver, 10).until(EC.url_contains("the_form_processor"))
    assert "the_form_processor" in driver.current_url

    # Проверки результата
    assert driver.find_element(By.ID, "_valueusername").text.strip() == "autotester"
    assert driver.find_element(By.ID, "_valuepassword").text.strip() == "12345"
    assert driver.find_element(By.ID, "_valuecomments").text.strip() == "Это автотест"
    assert driver.find_element(By.ID, "_valuecheckboxes0").text.strip() == "cb1"
    assert driver.find_element(By.ID, "_valuecheckboxes1").text.strip() == "cb3"
    assert driver.find_element(By.ID, "_valueradioval").text.strip() == "rd2"
    assert driver.find_element(By.ID, "_valuedropdown").text.strip() == "dd4"

    driver.quit()


