#Lv.1

number_of_people = 0

'''
return 반환은 () 괄호를 빼고, 전역변수 number_of_people을 돌려줘야 한다
increase_user은 단순 함수명이고, 
def increase_user(number_of_people) 처럼 쓰면, 해당 함수 안에서만 쓰는 잘못된 가짜변수를 만든 것 !!
return () => return number_of people
''' 
def increase_user():
    global number_of_people
    number_of_people += 1

    return number_of_people

# 근데 함수 호출할 때는 왜 인자 없이 호출해야되는걸까...
# => 애초에 def increase_number() 때부터 외부 인자 없이 알아서 작동하는 함수로 위에서 설정됐기 때문이다

result = increase_user()

# print로 ({어떤 문구or멘트}+{출력값} 이렇게 출력하게 만들고 싶으면, 
# 반드시 <<문자열과 변수(result 등) 사이에 ,(콤마)를 넣어줘야 한다>>
print('현재 가입 된 유저 수: ' , result)
