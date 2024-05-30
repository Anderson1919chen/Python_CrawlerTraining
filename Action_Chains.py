# 爬取ig關鍵字圖片
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import requests
import os
import wget

option = webdriver.EdgeOptions()
option.add_experimental_option("detach", True)
s = Service(executable_path=r"C:/Users/User/Desktop/edgedriver1/msedgedriver.exe")
driver = webdriver.Edge(options=option,service=s)

# 登入ig
driver.get("https://www.instagram.com/?hl=zh-tw")
username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username"))
)
password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "password"))
)
login = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]')
username.clear()
password.clear()
username.send_keys("anderson1233211234567@gmail.com")
password.send_keys("andersonsmalljay1234")
login.click()
time.sleep(5)

# 在google上搜尋cat並儲存圖片
driver.get("https://google.com")
search = driver.find_element(By.CLASS_NAME, "gLFyf")
search.clear()
keyword = "cat"
search.send_keys(keyword)
search.send_keys(Keys.RETURN)

pictrue = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="hdtb-sc"]/div/div/div[1]/div/div[2]/a/div'))
)
pictrue.click()
images = driver.find_elements(By.CLASS_NAME, "YQ4gaf")

if not os.path.exists(keyword):
    os.makedirs(keyword)

count = 0
#for img in images:    
    #src = img.get_attribute("src") or img.get_attribute("data-src")
    #save_as = os.path.join("C:/Users/User/Desktop/selenium_tutorial", keyword , f"{keyword}{count}.jpg")
    #wget.download(src , out = save_as)
    #count += 1
    
for img in images:    
    src = img.get_attribute("src") or img.get_attribute("data-src")
    if src:
        save_as = os.path.join("C:/Users/User/Desktop/selenium_tutorial", keyword , f"{keyword}{count}.jpg")
        try:
            wget.download(src , out = save_as)
            print(f"Image saved as: {save_as}")
        except Exception as e:
            print(f"Failed to download {src}. Error: {e}")
        count += 1

time.sleep(5)
driver.quit()


