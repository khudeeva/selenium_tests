from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
def test_full_form_myself():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://testpages.herokuapp.com/styled/basic-html-form-test.html")

    driver.find_element(By.NAME, "username").send_keys("qa_autotest")
    driver.find_element(By.NAME, "password").send_keys("qwerty")

    textarea = driver.find_element(By.NAME, "comments")
    textarea.clear()
    textarea.send_keys("повторная проверка формы")

    checkbox2 = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox'][value='cb2']")
    if not checkbox2.is_selected():
        checkbox2.click()

    radio = driver.find_element(By.CSS_SELECTOR, "input[name='radioval'][value = 'rd1']")
    radio.click()

    dropdown = Select(driver.find_element(By.NAME, "dropdown"))
    dropdown.select_by_value("dd5")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='submit'][name='submitbutton']"))
    )
    driver.find_element(By.CSS_SELECTOR, "input[type='submit'][name='submitbutton']").click()

    assert driver.find_element(By.ID, "_valueusername").text.strip() == "qa_autotest"
    assert driver.find_element(By.ID, "_valuepassword").text.strip() == "qwerty"
    assert driver.find_element(By.ID, "_valuecomments").text.strip() == "повторная проверка формы"
    assert driver.find_element(By.ID, "_valuecheckboxes0").text.strip() == "cb2"
    assert driver.find_element(By.ID, "_valueradioval").text.strip() == "rd1"
    assert driver.find_element(By.ID, "_valuedropdown").text.strip() == "dd5"

    driver.quit()