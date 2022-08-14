import pandas as pd

test_17 = pd.read_csv('./source/제주특별자치도_주제1_제주 예비창업자를 위한 업종별 카드 매출과 매장수 데이터 활용_매쉬업결과_17.csv',encoding='cp949')
test_18 = pd.read_csv('./source/제주특별자치도_주제1_제주 예비창업자를 위한 업종별 카드 매출과 매장수 데이터 활용_매쉬업결과_18.csv',encoding='cp949')
test_19 = pd.read_csv('./source/제주특별자치도_주제1_제주 예비창업자를 위한 업종별 카드 매출과 매장수 데이터 활용_매쉬업결과_19.csv',encoding='cp949')
test_20 = pd.read_csv('./source/제주특별자치도_주제1_제주 예비창업자를 위한 업종별 카드 매출과 매장수 데이터 활용_매쉬업결과_20.csv',encoding='cp949')
test_21 = pd.read_csv('./source/제주특별자치도_주제1_제주 예비창업자를 위한 업종별 카드 매출과 매장수 데이터 활용_매쉬업결과_21.csv',encoding='cp949')

df = pd.concat([test_17,test_18,test_19,test_20,test_21],axis=0)
df1 = df[df['업종명']=='비알콜 음료점업'].drop(columns=['업종코드','업종명 대분류','데이터기준일자','업종명','이용자수','이용건수']).reset_index(drop=True)
# 결측치 처리
df1['연령대'] = df1['연령대'].fillna('단체')
df1['관광구분'] = df1['관광구분'].fillna('불분명')
# csv 파일로 저장
df1.to_csv('지역별 카드 매출 데이터.csv',encoding='utf-8-sig',index=False)