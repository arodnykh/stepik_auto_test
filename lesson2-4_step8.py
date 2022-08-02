from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

def calc(x1):
    return str(math.log(abs(12*math.sin(int(x1)))))

# говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельной
WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
button =  browser.find_element(By.ID,"book")
button.click()

x = browser.find_element(By.ID, "input_value")
x1 = x.text
y = calc(x1)

input1 = browser.find_element(By.ID, "answer")
input1.send_keys(y)

btn =  browser.find_element(By.ID,"solve")
btn.click()

time.sleep(10) 

browser.quit()