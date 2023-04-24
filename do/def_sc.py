import mysql.connector
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome import service as fs #DeprecationWarning対策
import math

def mysqlconnect():
    cnx = mysql.connector.connect(
    user='root',  # ユーザー名
    password='beXEqA0XTZTHkCexUcJk',  # パスワード
    host='web-scraping-db.chi0mlgcsg5p.ap-northeast-1.rds.amazonaws.com',  # ホスト名(IPアドレス）
    #database ='WEBSCRAPING'
    )
    if cnx.is_connected:
            print("Connected!")
            
    return(cnx)

def chrome():
    CHROMEDRIVER = "/usr/local/bin/chromedriver"
    chrome_service = fs.Service(executable_path=CHROMEDRIVER)
    options = Options()
    options.add_argument(f'service={chrome_service}')
    options.headless = True
    driver = webdriver.Chrome(service=chrome_service,options=options)
    return(driver)

def pages(hit):
    if((hit % 20) == 0):
        pages = hit/20
    else:
        pages = math.floor(hit / 20 + 1)
    
    return(pages)