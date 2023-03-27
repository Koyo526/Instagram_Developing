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

def send_DM():
    # url
    url = "https://www.instagram.com/"
    #ユーザーネーム
    username="camcolle_koyo"
    #パスワード
    password="Koyo0526"
    #定型文
    text1="突然フォローごめんなさい！"
    text2="秋田県立大学3年のこーよーです！"
    text3="今、秋田のイベントで、ダンスの企画の出演者を募集してます！"
    text4="初心者も経験者も大歓迎です！よろしければ詳しい話聞いてみませんか？"
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
    df_guest=pd.read_csv("Unsent_list.csv")
    df_guest=df_guest['Name'].tolist()
    sent_list=[]
    i=0
    for guset in df_guest:
        driver.get('https://www.instagram.com/' + guset + '/')
        time.sleep(3)
        message_box = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button")
        message_box.click()
        time.sleep(3)
        if(i==0):
            on_box = driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/button[2]")
            on_box.click()
        text_box = driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
        text_box.send_keys(text1) 
        text_box.send_keys(text2)
        send_box = driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button")
        send_box.click()
        text_box = driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
        text_box.send_keys(text3)
        text_box.send_keys(text4)
        send_box = driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button")
        send_box.click()
        sent_list.append(guset)
        i+=1
    df_guset=pd.Series(sent_list,name='Name')
    df_guset.to_csv("Today_sent_list.csv",index=False)

if __name__ == '__main__':
    send_DM()