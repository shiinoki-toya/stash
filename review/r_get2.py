from re import U
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service as fs #DeprecationWarning対策
from selenium.webdriver.chrome.options import Options
from platform import python_branch
import mysql.connector
import logging
import time
import math
cnx = None

link = "https://travel.yahoo.co.jp/area/ma000000/?adc=1&discsort=1&kwd=%E3%83%AB%E3%83%BC%E3%83%88%E3%82%A4%E3%83%B3&lc=1&per_page=20&pn=1&ppc=2&rc=1&si=6"
link1st = "https://travel.yahoo.co.jp/area/ma000000/p"
link2nd = "/?adc=1&discsort=1&kwd=%E3%83%AB%E3%83%BC%E3%83%88%E3%82%A4%E3%83%B3&lc=1&per_page=20&ppc=2&rc=1&si=6"
url = []
hotelurl =[] 

try:
    cnx = mysql.connector.connect(
        user='root',  # ユーザー名
        password='eV9RW!_C',  # パスワード
        host='127.0.0.1',  # ホスト名(IPアドレス）
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
    driver.get(link)
    
    time.sleep(2)
    hitcounter = driver.find_element(by = By.CSS_SELECTOR, value = ".counter_agvsc")
    hit = int(hitcounter.text)
    
    if((hit % 20) == 0):
        pages = hit/20
    else:
        pages = math.floor(hit / 20 + 1)
    
    for i in range(pages):
        if(i == 0):
            hotelurl.append(link)
        else:
            nlink = link1st + str(i+1) + link2nd
            hotelurl.append(nlink)
            
   
            
            
    for i in range(1):#page数len(hotelurl)
        CHROMEDRIVER = "/usr/local/bin/chromedriver"
        chrome_service = fs.Service(executable_path=CHROMEDRIVER)
        options = Options()
        options.add_argument(f'service={chrome_service}')
        options.headless = True
        driver = webdriver.Chrome(service=chrome_service,options=options)
        
        driver.get(hotelurl[i])
        urls = driver.find_elements(by = By.CSS_SELECTOR, value = ".anchor.morePlans")
        #urlをホテルの数だけ取得して、配列に格納
        for j in range(len(urls)):
            url.append(urls[j].get_attribute("href"))
            
            if('discsort=1&lc=1&ppc=2&rc=1&st=1&' in url[j]):
                url[j] = url[j].replace('?discsort=1&lc=1&ppc=2&rc=1&st=1&top=rooms','review/')
            else:
                url[j] = url[j].replace('?top=rooms','review/')
                
                
        for k in range(1):#len(urls)
            #print(url[k])
            driver.get(url[k])
            review = driver.find_elements(by = By.CSS_SELECTOR, value = ".text-gray-800.text-lg")
            point = driver.find_elements(by = By.CSS_SELECTOR, value = "span.text-3xl")
            date = driver.find_elements(by = By.CSS_SELECTOR, value = 'span[itemprop="datePublished"]')
            
            n=1
            
            for element in review:
                if not element.text:
                    pass
                else:
                    cursor = cnx.cursor()
                    sql = ("""
                            INSERT INTO trn_scraping_details
                            (customer_code,scraping_exe_information,scraping_exe_html_result)
                            VALUES (100000,%s,%s)
                            """)
                    data = [(n,element.text)]
                    cursor.executemany(sql,data)
                    n= n+1
            
            n=1

            for element in point:
                if not element.text:
                    pass
                else:
                    cursor = cnx.cursor()
                    sql = ("""
                            INSERT INTO trn_scraping_details
                            (customer_code,scraping_exe_information,scraping_exe_html_result)
                            VALUES (100000,%s,%s)
                            """)
                    data = [(n,element.text)]
                    cursor.executemany(sql,data)
                    n= n+1
            
            n=1

            for element in date:
                if not element.text:
                    pass
                else:
                    cursor = cnx.cursor()
                    sql = ("""
                            INSERT INTO trn_scraping_details
                                (customer_code,scraping_exe_information,scraping_exe_html_result)
                            VALUES (100000,%s,%s)
                            """)
                    data = [(n,element.text)]
                    cursor.executemany(sql,data)
                    n= n+1                 
        
        
        
        cnx.commit()
        cursor.close()    
        elements = None
        urls = None
        url = None
        url = []
        driver.quit()
        print(i)
        
        
except:
    logging.error("traceback",exc_info=True)

finally:
    driver.quit()
    if cnx is not None and cnx.is_connected():
        cnx.close()