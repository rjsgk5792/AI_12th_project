import time
import sys 
import os 

import pandas as pd
import numpy as np

from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import warnings
warnings.filterwarnings('ignore')

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)
query = '제주 카페'
driver.get(f"https://map.naver.com/v5/search/{query}?c=14203933.7141038,4562681.4505997,10,0,0,0,dh")

driver.find_ele


#스크롤 내리기 이동 전 위치 
scroll_location = driver.execute_script("return document.body.scrollHeight") 
while True: 
    #현재 스크롤의 가장 아래로 내림 
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)") 
    #전체 스크롤이 늘어날 때까지 대기 
    time.sleep(2) 
    #늘어난 스크롤 높이 
    scroll_height = driver.execute_script("return document.body.scrollHeight") 
    #늘어난 스크롤 위치와 이동 전 위치 같으면(더 이상 스크롤이 늘어나지 않으면) 종료 
    if scroll_location == scroll_height: break 
    #같지 않으면 스크롤 위치 값을 수정하여 같아질 때까지 반복
    else: 
        #스크롤 위치값을 수정 
        scroll_location = driver.execute_script("return document.body.scrollHeight")

