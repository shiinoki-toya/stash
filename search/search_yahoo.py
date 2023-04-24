from re import U
from wsgiref.validate import InputWrapper
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service as fs #DeprecationWarning対策
from selenium.webdriver.chrome.options import Options
import logging
import time
import math
import mysql.connector

cnx = None

url = "https://travel.yahoo.co.jp/"

try:
    cnx = mysql.connector.connect(
    user='root',  # ユーザー名
    password='n6H!gvB%',  # パスワード
    host='192.168.101.142',  # ホスト名(IPアドレス）
    database ='WEBSCRAPING'
    )
    if cnx.is_connected:
        print("Connected!")
    
    CHROMEDRIVER = "/usr/local/bin/chromedriver"
    chrome_service = fs.Service(executable_path=CHROMEDRIVER)
    options = Options()
    options.add_argument(f'service={chrome_service}')
    options.headless = True
    driver = webdriver.Chrome(service=chrome_service,options=options)
    driver.get(url)
    
    search_bar = driver.find_element(by=By.XPATH, value='//*[@id="__layout"]/div/div/main/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/div[1]/div/input')
    search_bar.send_keys("ルートイン")
    search_button =  driver.find_element(by=By.XPATH, value='//*[@id="__layout"]/div/div/main/div[2]/div[2]/div/div/div[1]/div[3]/button')
    search_button.click()
    time.sleep(2)
    
    
    cur_url = driver.current_url
    print(cur_url)
    
    driver.set_window_size(1024, 768)
    # 対象ページへアクセス
    # スクリーンショットを取得
    driver.save_screenshot('result.png')
    
except:
    logging.error("traceback",exc_info=True)

finally:
    driver.quit()