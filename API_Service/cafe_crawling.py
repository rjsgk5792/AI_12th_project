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
driver.get(f'https://map.naver.com/v5/search/{query}?c=14141917.7816301,4474909.6795512,15,0,0,0,dh')
# 검색결과 iframe 접근
driver.switch_to.frame("searchIframe")

title_list = []
location_list = []
f_data_list = []

try:
    for i in range(1,7):
        driver.find_element_by_link_text(str(i)).click()
        try:
            for j in range(3,70,3):
                element = driver.find_elements_by_css_selector('.OXiLu')[j]
                element.click()
                driver.implicitly_wait(10)
                location_list.append(driver.find_element_by_css_selector('._2yqUQ').text)
    
                ActionChains(driver).move_to_element(element).key_down(Keys.PAGE_DOWN).key_up(Keys.PAGE_DOWN).perform()
        except:
            pass
    
        ## 카페 이름 컬럼 리스트 생성
        title_raw = driver.find_elements_by_css_selector('.OXiLu')
        for title in title_raw:
            title = title.text
            title_list.append(title)
        
        ## 위치 컬럼 리스트 생성
        # location_raw = driver.find_elements_by_css_selector('._2yqUQ')
        # for loc in location_raw:
        #     loc = loc.text
        #     location_list.append(loc)

        # Feature 컬럼 리스트 생성
        data_raw = driver.find_elements_by_css_selector('._17H46')
        for data in data_raw:
            data = data.text
            f_data_list.append(data)
    
except:
    pass

print(len(title_list),len(location_list),len(f_data_list))

# 데이터 프레임 생성
df = pd.DataFrame({'카페이름':title_list, 'data': f_data_list})

no_visitor_review = df[~df['data'].str.contains('방문자리뷰')].index
no_blog_review = df[~df['data'].str.contains('블로그리뷰')].index
no_score_index = df[~df['data'].str.contains('별점')].index

# 별점, 리뷰 없는 데이터 제거
dropped_data = df.drop(index=no_score_index, axis=0)

# Feature 분할
data_list = dropped_data['data'].values.tolist()

# 별점, 방문자리뷰, 블로그리뷰 숫자만 남기고 제거
for i in range(len(data_list)):
    data_list[i] = data_list[i].split('별점')[1]
    data_list[i] = data_list[i].split('\n')[1]
    
    data_list[i] = data_list[i].replace('방문자리뷰','').replace('블로그리뷰','')
    data_list[i] = data_list[i].split(' ')

# 최종 데이터 프레임 생성
star = []
visitor = []
blog = []

for i in range(len(data_list)):
    star.append(data_list[i][0])
    visitor.append(data_list[i][1])
    blog.append(data_list[i][2])

cafe_df = dropped_data.drop(columns=['data'])

cafe_df['별점'] = star
cafe_df['방문자리뷰'] = visitor
cafe_df['블로그리뷰']= blog

# 크롤링 데이터 -> .csv 파일로 저장
cafe_df.to_csv(f"navermap_{query}", encoding='utf-8-sig',index=False)


'''
# .to_csv 누적 저장(크롤링)
# 최초 생성 이후 mode는 append
if not os.path.exists('output.csv'):
    df.to_csv('output.csv', index=False, mode='w', encoding='utf-8-sig')
else:
    df.to_csv('output.csv', index=False, mode='a', encoding='utf-8-sig', header=False)

'''
