# Lv.2
# pro_num = 1000
global_data = {'subject': 'python', 'day': 3, 'title': '함수 활용하기'}

"""
create_data 함수 정의 => 매개변수 작성
함수 내부에서 data 변수 작성 => 비어있는 dict를 할당받고, 
create_data 내부에 있는 매개변수들을 data 안에 할당한다
global pro_num 이고 pro_num += 1 

"""
# global_data가 아니라 그냥 global이라는걸 기억할 것

def create_data(subject,day,title=None):
    global pro_num
    pro_num += 1

# 딕셔너리에 value값은 따옴표 ('')를 빼야지 인식이 되지...안 그럼 그냥 텍스트임
    data = {'과목':subject, '일차':day, '제목':title, '문제번호': pro_num}

    return data

result_1 = create_data('python',3)
result_2 = create_data(subject='web', day=1, title='web 연습하기')
result_3 = create_data(**global_data)


#print 함수는 잊지말고 다 하자 !!!!!!!!!
print(result_1)
print(result_2)
print(result_3)

