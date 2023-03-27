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

df_guest=pd.read_csv("today_guset_list.csv")
df_guest=df_guest['Name'].tolist()
url_list=[]
instagram_id=[]
for guest in df_guest:
    url='https://www.instagram.com/' + guest + '/'
    url_list.append(url)
    id='@'+guest
    instagram_id.append(id)
df_url=pd.Series(url_list,name='URL')
df_url.to_csv("Guest_URL.csv",index=False)
df_id=pd.Series(instagram_id,name='ID')
df_id.to_csv("Guest_Instagram_ID.csv",index=False)
