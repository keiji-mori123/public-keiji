#from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.service import Service as ChromeService

#driver_location = (r"C:\\Users\\hayab\\Desktop\\ぱいそん\\chromedriver.exe")
#service = ChromeService(executable_path=r"C:\\Users\\hayab\\Desktop\\ぱいそん\\chromedriver.exe")
#driver = webdriver.Chrome(service=service)
#driver.implicitly_wait(15)
#driver.get("https://www.library.chiyoda.tokyo.jp/")

#千代田区立図書館の会館か閉館を見てみる　VER1
#shedule_el = driver.find_elements(By.CLASS_NAME, 'schedule-list01__text')
#print([s.text for s in shedule_el])
 
#VER2  限定してspanを取る
#shedule_el = driver.find_elements(
    #By.XPATH, '//*[@id="shohei-today-status"]/div[1]/div[1]/div/span')
#print([s.text for s in shedule_el])

##################ヘッドレス###################
#from selenium.webdriver.chrome.options import Options
#from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.service import Service as ChromeService
#import time

#options = Options()
#options.add_argument('--headless')

#driver_location = (r"C:\\Users\\hayab\\Desktop\\ぱいそん\\chromedriver.exe")
#driver = webdriver.Chrome(service=ChromeService(
    #r'C:\\Users\\hayab\\Desktop\\ぱいそん\\chromedriver.exe'),options=options)
#time.sleep(10)
#driver.get("https://www.library.chiyoda.tokyo.jp/")

#shedule_el = driver.find_elements(
    #By.XPATH, '//*[@id="shohei-today-status"]/div[1]/div[1]/div/span')
#print([s.text for s in shedule_el])

###########文字入力############
#driver.get("https://www.library.chiyoda.tokyo.jp/")

#el = driver.find_element(By.ID,"〇〇")
#el.send_keys("ぱすわーどなど")

###########入力済みの文字を削除(空欄にする)###########
#driver.get("https://www.library.chiyoda.tokyo.jp/")

#el = driver.find_element(By.ID,"〇〇")
#el.clear()

###########クリック##########
#driver.get("https://www.library.chiyoda.tokyo.jp/")

#el = driver.find_element(By.ID,"〇〇")
#el.click()

#########ドロップダウン#########
#from selenium.webdriver.support.ui import Select

#driver.get("https://www.library.chiyoda.tokyo.jp/")

#el = driver.find_element(By.ID,"〇〇")
#s = Select(el)
#s.select_by_value("1")

###本を検索していく###
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
import time
from selenium.webdriver.support.ui import Select

options = Options()
options.add_argument('--headless')

driver_location = (r"C:\\Users\\hayab\\Desktop\\ぱいそん\\chromedriver.exe")
driver = webdriver.Chrome(service=ChromeService(
    r'C:\\Users\\hayab\\Desktop\\ぱいそん\\chromedriver.exe'),options=options)
time.sleep(10)
driver.get("https://www.library.chiyoda.tokyo.jp/")

text_box = driver.find_element(By.NAME,"txt_word")
text_box.send_keys("pythonプログラミング")
time.sleep(10)
btn = driver.find_element(By.NAME, "submit_btn_searchEasy")
btn.click()

#さらに昇順、降順のドロップダウン(Slect)で、昇順にする。
time.sleep(10)
oder = driver.find_element(By.ID,"opt_oder")
oder_select = Select(oder)
oder_select.select_by_value("0")

#再表示をクリック
time.sleep(3)
btn_sort = driver.find_element(By.NAME,"submit_btn_sort")
btn_sort.click()

#スクショ
time.sleep(3)
driver.save_screenshot("result.png")
