import requests
from pprint import pprint

# 문제4. C번의 데이터를 활용하여, 섭씨 온도 데이터를 추가합니다.

def get_result(api_key):

    lat = 37.56
    lon = 126.97
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"

    json_response = requests.get(url).json()

    main_data = json_response.get('main')
    weather_data = json_response.get('weather')[0] 

    temp_c = round(main_data['temp'] - 273.15, 2)
    feels_like_c = round(main_data['feels_like'] - 273.15, 2)
    temp_max_c = round(main_data['temp_max'] - 273.15, 2)
    temp_min_c = round(main_data['temp_min'] - 273.15, 2)

    result = {
        '기본': {
            '기압': main_data['pressure'],
            '습도': main_data['humidity'],
            '온도': main_data['temp'],
            '온도(섭씨)': temp_c,
            '체감온도': main_data['feels_like'],
            '체감온도(섭씨)': feels_like_c,
            '최고온도': main_data['temp_max'],
            '최고온도(섭씨)': temp_max_c,
            '최저온도': main_data['temp_min'],
            '최저온도(섭씨)': temp_min_c
        },
        '날씨': [  
            {
                '요약': weather_data['description'],
                '아이콘': weather_data['icon'],
                '핵심': weather_data['main'],
                '식별자': weather_data['id']
            }
        ]
    }

    return result

api_key = '823314acf564bf12335241c968aaa8a6'

# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_result(api_key)
    # pprint.pprint(): json 을 보기 좋은 형식으로 출력
    pprint(result)