import pandas as pd
import numpy as np
import pickle


df = pd.read_csv('/Users/rjsgk/section3/web_workspace/postgreSQL/지역별 카드 매출 데이터.csv')

X = df[['시도명','지역구분','연령대','이용자구분']]
y = df['읍면동명']

from sklearn.preprocessing import LabelEncoder
from category_encoders import OrdinalEncoder
le = LabelEncoder()
ord = OrdinalEncoder()
X = ord.fit_transform(X)
y = le.fit_transform(y)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

from sklearn.svm import SVC
sv = SVC(kernel='linear').fit(X_train,y_train)


pickle.dump(sv, open('cafe.pkl', 'wb'))
