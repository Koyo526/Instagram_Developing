from numpy import select
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import urllib.parse
import re
import json
import chromedriver_binary 
import datetime
import time
import pandas as pd
import random
import sys
def now_time():
   '''
   現在の時間を表示する関数
   '''
   dt_now = datetime.datetime.now()
   return dt_now.strftime('%m/%d %H:%M')
def login_instagram():
    # url
    url = "https://www.instagram.com/"
    #ユーザーネーム
    username=""
    #パスワード
    password=""
    #ハッシュタグ検索
    tagu=""
    # ブラウザーを起動
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(10)  # 見つからないときは、10秒まで待つ
    #ユーザーネーム入力
    id_box = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
    id_box.send_keys(username)
    #パスワード入力
    id_pass = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
    id_pass.send_keys(password)
    #ログインボタンをクリック
    lg_box = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button")
    lg_box.click()
    # 3秒スリープ（待機）
    time.sleep(10)
    # 対象アカウントのInstagramページにアクセス
    driver.get('https://www.instagram.com/' + username + '/')
    time.sleep(3)
    # 画面上で、フォローのリンクをクリック
    follower_button = driver.find_elements_by_css_selector("li.Y8-fY")[2]
    follower_button.click()
 
    # 3秒スリープ（待機）
    time.sleep(3)

    #ハッシュタグ検索
    sreach_tagu=driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")
    sreach_tagu.send_keys(tagu)

               
if __name__ == '__main__':
    login_instagram()
