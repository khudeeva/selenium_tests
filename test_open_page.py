from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://duckduckgo.com")
time.sleep(2)

# Обновлённый способ найти поле поиска
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium Python")
search_box.send_keys(Keys.RETURN)
time.sleep(3)

# Проверим, что появились результаты
results = driver.find_elements(By.CSS_SELECTOR, "article")
assert len(results) > 0
print("✅ Результаты найдены!")

driver.quit()



