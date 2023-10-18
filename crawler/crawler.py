from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
import cv2
import numpy as np

driver = webdriver.Chrome()
driver.get("https://image.baidu.com/")
driver.find_element(By.ID, "kw").send_keys("刘亦菲")
button = driver.find_element(By.CLASS_NAME, "s_newBtn")
button.click()
time.sleep(3)
lis = driver.find_elements(By.TAG_NAME, "li")
for i, li in enumerate(lis):
    url = li.get_attribute("data-objurl")
    ext = li.get_attribute("data-ext")
    if url is not None and ext == "jpg":
        print(url)
        b = requests.get(url).content
        img = cv2.imdecode(np.frombuffer(b, np.uint8), cv2.IMREAD_COLOR)
        cv2.imwrite(f"outputs/{i}.jpg", img)
        # cv2.imshow("w", img)
        # cv2.waitKey()