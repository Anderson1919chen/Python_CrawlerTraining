from selenium import webdriver 
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import requests

option = webdriver.EdgeOptions()
option.add_experimental_option("detach", True)
s = Service(executable_path=r"C:/Users/User/Desktop/edgedriver1/msedgedriver.exe")
driver = webdriver.Edge(options=option,service=s)

# google搜尋比特幣
#driver.get("HTTPS://google.com")
#search = driver.find_element(By.CLASS_NAME, "gLFyf")
#search.clear()
#search.send_keys("比特幣")
#search.send_keys(Keys.RETURN) #按下鍵盤上的ENTER
#time.sleep(2)
#titles = driver.find_elements(By.XPATH, "//h3")
#for title in titles:
#    print(title.text)# 取得標籤內部的文字

# ptt
driver.get("https://www.ptt.cc/bbs/index.html")
link = driver.find_element(By.CLASS_NAME, "board-name")
link.click()
button = driver.find_element(By.CLASS_NAME, "btn-big")
button.click()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "board"))#等到頁面上的class=board出現才會繼續執行
)

titles_ptt = driver.find_elements(By.NAME, "title")
for title_ptt in titles_ptt:
    print(title_ptt.text)

page = driver.find_element(By.LINK_TEXT, "‹ 上頁")
page.click()

time.sleep(5)
driver.quit()
