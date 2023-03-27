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


def change_ID_to_list():
    df_ID=pd.read_csv("Guest_Instagram_ID.csv")
    df_ID=df_ID['ID'].tolist()
    Unsent_list=[]
    for guest in df_ID:
        Unsent_list.append(guest[1:])
    print(Unsent_list)
    df_send=pd.Series(Unsent_list,name='Name')
    df_send.to_csv("Unsent_list.csv",index=False)

if __name__=='__main__':
    change_ID_to_list()
        


