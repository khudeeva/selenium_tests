from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
import logging

logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s-%(message)s'
)
def test_mix_with_logging():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    logging.info("Открыта страница checkboxes")

    checkbox2 = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")[1]
    if not checkbox2.is_selected():
        checkbox2.click()
        logging.info("Кликаем на чекбокс 2")
    assert checkbox2.is_selected()
    logging.info("Проверка, что чекбокс 2 выбран")

    driver.get("https://demoqa.com/radio-button")
    logging.info("Открыта страница Radio Button")
    driver.find_element(By.XPATH, "//label[text()='Yes']").click()
    logging.info("Кликаем по тексту Yes")
    text = driver.find_element(By.CLASS_NAME, "text-success")
    logging.info("Ищем текст под кнопкой")
    assert text.text.strip() == "Yes"
    logging.info("Проверка, сто текст под кнопкой 'Yes'")

    driver.get("https://the-internet.herokuapp.com/dropdown")
    logging.info("Открыта страница Dropdown List")
    dropdown = Select(driver.find_element(By.ID, "dropdown"))
    dropdown.select_by_value("2")
    logging.info("Выбираем Option2")
    selected = dropdown.first_selected_option
    assert selected.text.strip() == "Option 2"
    logging.info("Проверка, что Option2 выделен в списке")

    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    logging.info("Открыта страница JavaScript Alerts")
    driver.find_element(By.CSS_SELECTOR, "button[onclick='jsPrompt()']").click()
    logging.info("Нажата кнопка 'Click for js Prompt'")
    alert = driver.switch_to.alert
    logging.info("Переключаемся на alert")
    alert.send_keys("Ksenia")
    logging.info("Вводим в alert 'Ksenia'")
    alert.accept()
    logging.info("Alert принят")
    result = driver.find_element(By.ID, "result")
    assert result.text.strip() == "You entered: Ksenia"
    logging.info("Проверка, что введенный текст совпадает")

    driver.quit()
    logging.info("Тест завершен, браузер закрыт")