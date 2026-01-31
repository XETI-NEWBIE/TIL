
import requests
from pprint import pprint as print

# 무작위 유저 정보 요청 경로
API_URL = 'https://jsonplaceholder.typicode.com/users/'
# API 요청
response = requests.get(API_URL)
# # JSON -> dict 데이터 변환
name = response.json()
dummy_data = []

for i in range(1,11):
    api_new = API_URL+str(i)
    response = requests.get(api_new)
    user_data = response.json()
    name = user_data['name']
    dummy_data.append(name)
print(dummy_data)

