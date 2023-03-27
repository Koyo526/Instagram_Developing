from numpy import select
from w import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import urllib.parse
import re
import json
import chromedriver_binary  
from webdriver_manager.chrome import ChromeDriverManager
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
    username="camcolle_koyo"
    #パスワード
    password="Koyo0526"
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
 
    # フォロワーの一覧は、ポップアップウインドウで表示されます
    dialog = driver.find_element_by_css_selector("div.PZuss")
    for i in range(500):
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", dialog)
        time.sleep(random.randint(500,1000)/1000)
 
    page_url = driver.page_source
    soup = BeautifulSoup(page_url,"lxml")
    elements = soup.find_all("a", {"class": "FPmhX notranslate _0imsa"})
    followes = []
    # 取得できたフォロー名を配列にadd
    for value in elements:
        followes.append(value.text)
    # csvに書き出し
    df_follows= pd.Series(followes,name='Name')
    df_follows.to_csv(username + '_follows_list.csv',index=False)
    df_send=pd.read_csv("send_list.csv")
    send_list=df_send['Name'].tolist()
    df_staff=pd.read_csv("staff_list.csv")
    staff_list=df_staff['Name'].tolist()
    guset_list=[]
    for list in followes:
        if list in send_list:
            pass
        elif list in staff_list:
            pass
        else:
            guset_list.append(list)

    df_guset=pd.Series(guset_list,name='Name')
    df_guset.to_csv("today_guset_list.csv",index=False)
               
if __name__ == '__main__':
    login_instagram()