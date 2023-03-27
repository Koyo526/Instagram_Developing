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


def change_guest_to_send():
    df_guest=pd.read_csv("today_guset_list.csv")
    df_guest=df_guest['Name'].tolist()
    df_send=pd.read_csv("send_list.csv")
    send_list=df_send['Name'].tolist()
    for guest in df_guest:
        send_list.append(guest)
    print(send_list)
    df_send=pd.Series(send_list,name='Name')
    df_send.to_csv("send_list.csv",index=False)

if __name__=='__main__':
    change_guest_to_send()


