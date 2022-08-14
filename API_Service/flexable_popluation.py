import requests
import json

start_date = 20170101
end_date = 20191231
# city = 
# emd = 동
# gender = 
# age = 
# number = Cnt 개수
# limit 

API_URL = f'https://open.jejudatahub.net/api/proxy/Daaa1t3at3tt8a8DD3t55538t35Dab1t/19crpo__tr1_39_90111tc1p951ttb51?startDate={start_date}&endDate={end_date}&city=제주'
res = requests.get(API_URL)
parsed_data = json.loads(res.text)
print(parsed_data)
