from selenium import webdriver
from selenium.webdriver.common.by import By
import time 


try:
    link = "https://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.XPATH, "//div[@class='first_block']//input[contains(@class,'first')]")
    input1.send_keys("Тестовый ответ")

    input2 = browser.find_element(By.XPATH, "//div[@class='first_block']//input[contains(@class,'second')]")
    input2.send_keys("Тестовый ответ")

    input3 = browser.find_element(By.XPATH, "//div[@class='first_block']//input[contains(@class,'third')]")
    input3.send_keys("Тестовый ответ")
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
   
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

