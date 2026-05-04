import requests
from pprint import pprint

# 문제3. B번에서 얻는 결과를 활용하여, KEY 값들을 한글로 변경한 딕셔너리를 반환하도록 구성합니다.
# KEY 에 해당하는 한글 KEY 값들은 다음과 같습니다.
# feels_like : '체감온도',
# humidity : '습도',
# pressure : '기압',
# temp : '온도',
# temp_max : '최고온도',
# temp_min : '최저온도',
# description : '요약',
# icon : '아이콘',
# main : '핵심’
# id : ‘식별자’
def get_result(api_key):
    

# 요구사항에 맞도록 이곳의 코드를 수정합니다.
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"

    response = requests.get(url).json()

    result = {'main': response.get('main'), 
            'weather' : response.get('weather')}

    weather_info = {
        '체감온도' : result['main']['feels_like'],
        '습도' : result['main']['humidity'],
        '기압' : result['main']['pressure'],
        '온도' : result['main']['temp'],
        '최고온도' : result['main']['temp_max'],
        '최저온도' : result['main']['temp_min'],
        '요약' : result['weather'][0]['description'],
        '아이콘' : result['weather'][0]['icon'],
        '핵심' : result['weather'][0]['main'],
        '식별자' : result['weather'][0]['id']
    }

    return weather_info

#여러분의 OpenWeatherMap API 키를 설정하세요
api_key = '65d258f60ec8d9d6c9d7e637e0846059'
lat = 37.65
lon = 126.97

#아래 코드는 수정하지 않습니다.
if __name__ == '__main__':

# json 형태의 데이터 반환
    result = get_result(api_key)

# prrint.prrint(): json 을 보기 좋은 형식으로 출력
    pprint(result)
