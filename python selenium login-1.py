from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')

browser_location = (r"C:\\〇〇\\〇〇\\chromedriver.exe")
browser = webdriver.Chrome(service=ChromeService(r"C:\\〇〇\\〇〇\\chromedriver.exe"),options=options)
browser.get('https://〇〇〇/login_page')

from selenium.webdriver.common.by import By
import time

time.sleep(10)

elem_username = browser.find_element(By.ID, "username")
elem_username.send_keys('〇〇')

elem_password = browser.find_element(By.ID, "password")
elem_password.send_keys('〇〇')

elem_login_btn = browser.find_element(By.ID, "login-btn")
elem_login_btn.click()

browser.quit()