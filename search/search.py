from re import U
from wsgiref.validate import InputWrapper
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service as fs #DeprecationWarning対策
from selenium.webdriver.chrome.options import Options
import logging
import time
import math

url = "https://www.google.com/"

try:
    CHROMEDRIVER = "/usr/local/bin/chromedriver"
    chrome_service = fs.Service(executable_path=CHROMEDRIVER)
    options = Options()
    options.add_argument(f'service={chrome_service}')
    options.headless = True
    driver = webdriver.Chrome(service=chrome_service,options=options)
    driver.get(url)
    
    search_bar = driver.find_element(by=By.TAG_NAME, value="input")
    search_bar.send_keys("python")
    search_bar.submit()
    
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