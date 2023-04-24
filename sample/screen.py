from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome import service as fs
 
CHROMEDRIVER = "/usr/local/bin/chromedriver"
URL = "https://example.com/"
 
# ドライバー指定でChromeブラウザを開く
chrome_service = fs.Service(executable_path=CHROMEDRIVER)
 
options = Options()
options.add_argument(f'service={chrome_service}')
# ブラウザを表示しない
options.headless = True
 
driver = webdriver.Chrome(options=options)
 
# ウィンドウサイズ＝画像サイズ
driver.set_window_size(1024, 768)
# 対象ページへアクセス
driver.get(URL)
# スクリーンショットを取得
driver.save_screenshot('result.png')
 
driver.quit()
