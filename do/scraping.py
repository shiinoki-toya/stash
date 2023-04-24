from re import U
from selenium.webdriver.common.by import By
import logging
from selenium.webdriver.common.keys import Keys
import time

import def_sc

hotelurl =[] 
pageurl = []

url = "https://travel.yahoo.co.jp/"

try:
    cnx = def_sc.mysqlconnect()
    
    driver = def_sc.chrome()
    print(driver)
    driver.get(url)
    
    search_bar = driver.find_element(by=By.XPATH, value='//*[@id="__layout"]/div/div/main/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/div[1]/div/input')
    search_bar.send_keys("東急") #検索ワード
    search_bar.send_keys(Keys.ENTER)
    time.sleep(5)
    
    cur_url = driver.current_url
    strcount = cur_url.find('pn=')
    #print(strcount)
    
    hitcounter = driver.find_element(by = By.CSS_SELECTOR, value = ".counter_agvsc")
    hit = int(hitcounter.text)
    
    pages = def_sc.pages(hit)
    
    for i in range(1,pages):
        if(i == 1):
            pageurl.append(cur_url)
        else:
            nlink = cur_url[:(strcount+3)] + str(i) +  cur_url[(strcount+4):]
            #print(nlink)
            pageurl.append(nlink)
    
            
    for i in range(len(pageurl)):
        if i == 0:
            urls = driver.find_elements(by = By.CSS_SELECTOR, value = ".anchor.morePlans")
        else:
            driver.get(pageurl[i])
            urls = driver.find_elements(by = By.CSS_SELECTOR, value = ".anchor.morePlans")
        
        for element in urls:
            hotelurl.append(element.get_attribute("href")[:36])
            print(element.get_attribute("href")[:36])
    
    

    
except:
    logging.error("traceback",exc_info=True)

finally:
    driver.quit()