from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    img_box = browser.find_element(By.CSS_SELECTOR, "[id='treasure']")
    x = img_box.get_attribute("valuex")

    y = calc(x)
    
    input1 = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
    input1.send_keys(y)

    checkbox = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    checkbox.click()

    
    radio = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
    radio.click()
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
    button.click()
    
    time.sleep(10)

       
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

