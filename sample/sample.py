from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service as fs #DeprecationWarning対策
from selenium.webdriver.chrome.options import Options
import logging

CHROMEDRIVER = "/usr/bin/chromedriver"
chrome_service = fs.Service(executable_path=CHROMEDRIVER)
options = Options()
options.add_argument(f'service={chrome_service}')
options.headless = True
driver = webdriver.Chrome(service=chrome_service,options=options)
URL = "https://example.com/"

try:
    driver.set_window_size(1024, 768)

    driver.get(URL)

    driver.save_screenshot('result.png')
 
    driver.quit()
        
except:
    logging.error("traceback",exc_info=True)

finally:
    driver.quit()