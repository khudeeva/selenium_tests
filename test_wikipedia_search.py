from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# запуск браузера
service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service)

# открываем сайт
driver.get("https://ru.wikipedia.org")
time.sleep(2)

# ищем поле поиска
search_box = driver.find_element(By.NAME, "search")
search_box.send_keys("Python")
search_box.send_keys(Keys.RETURN)
time.sleep(2)

# проверяем, что заголовок страницы содержит "Python"
assert "Python" in driver.title
print("✅ Найдена страница с результатом!")

# закрываем браузер
driver.quit()
