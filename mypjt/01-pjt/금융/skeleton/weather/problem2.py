

import requests
from pprint import pprint

# 문제2. 날씨 데이터 중 다음 조건에 해당하는 값만 딕셔너리 형태로 반환하는 함수를 구성합니다.

def get_result(api_key):
    city_name = "Seoul,KR"
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=823314acf564bf12335241c968aaa8a6'

    response = requests.get(url).json()

    result = {'main': response.get('main'), 
              'weather' : response.get('weather')}

#   KEY 값이 “main” 인 데이터
#   KEY 값이 “weather” 인 데이터
# 함수에서 두 데이터를 새로운 dictionary 에 담아서 return 합니다.
# 요구사항에 맞도록 이곳의 코드를 수정합니다.

    return result

    pprint(response)

api_key = '823314acf564bf12335241c968aaa8a6'

# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_result(api_key)
    # prrint.prrint(): json 을 보기 좋은 형식으로 출력
    pprint(result)
