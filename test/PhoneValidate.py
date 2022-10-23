from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import ctypes  # An included library with Python install.

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://jinshuju.net/f/AyKW8br")
time.sleep(1)
text_phone = driver.find_element(By.NAME, "field_2")
text_phone.send_keys("phone number")
text_another = driver.find_element(By.NAME, "field_5")
text_another.click()
time.sleep(1)
el = driver.find_element(By.CLASS_NAME, "ant-form-item-explain-error")
if el is not None:
    ctypes.windll.user32.MessageBoxW(0, "测试成功！检测到警告框。", "Test Result", 0)
    time.sleep(1)
text_phone.clear()
text_phone.send_keys("18311268202")
text_another.click()
time.sleep(1)
el = driver.find_elements(By.CLASS_NAME, "ant-form-item-explain-error")
print(el)
time.sleep(1)
if len(el) == 0:
    ctypes.windll.user32.MessageBoxW(0, "测试成功！未检测到警告框。", "Test Result", 0)