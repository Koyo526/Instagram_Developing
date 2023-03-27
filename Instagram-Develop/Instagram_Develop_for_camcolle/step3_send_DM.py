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
def send_DM():

    #ユーザーネーム
    username=""   #ここは自分のInstagramのIDを入れてください 例 username="camcolle_akita"　こんな感じで「" "」の間に書いてください！
    #パスワード
    password=""   #ここは自分のInstagramのパスワードを入れてください！ 例 password="aktia21" こんな感じでIDと同じように「" "」の間に書いてください！
    #定型文
    text=""     #ここにDMで送る文章を書いてください！これまでと同じように「" "」の間に書いてください！　例　text="こんにちは！急にDM失礼します！..."

    
    
    url = "https://www.instagram.com/"  
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
        text_box.send_keys(text) 
        send_box = driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button")
        send_box.click()
        sent_list.append(guset)
        i+=1
    df_guset=pd.Series(sent_list,name='Name')
    df_guset.to_csv("Today_sent_list.csv",index=False)

if __name__ == '__main__':
    send_DM()