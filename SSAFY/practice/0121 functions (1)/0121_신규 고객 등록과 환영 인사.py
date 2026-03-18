# Lv.2 

number_of_people = 0

# 이 문제에서 increase_user()은 return 값이 필요가 없다

def increase_user():
    global number_of_people
    number_of_people += 1

# create_user가 햄버거라면, 
# increase_user 함수는 감자튀김.. 
# 원래 햄버거가 메인이고 감자튀김은 깔짝 등장만 해줘도 되는 것
# 유저를 등록(create) 하는 행위는 당연히 전체인원수를 세고 증가함(increase_user)까지 고려해야되니까, 
# 한 몸처럼 묶어주려고 create 함수 안에 increase_user()을 같이 넣어준 것 !

# 그리고 create_user(user_info)가 아닌 이유는 {name, age, address} 총 3개의 인자를
# 던져야되는데, 받는 매개변수를 user_info 하나만 뚫어놨기 때문..!!
# 야구공 3개(name/age/address)를 던졌는데 글러브 1개(user_info)로 받는 꼴이라는데, 아직 헷갈린다....

def create_user(name, age, address):
    increase_user()
    user_info = {'name': name, 'age': age, 'address': address}

    print(f'{name}님 환영합니다!')

    return user_info

print ('현재 가입된 유저 수 :', number_of_people)

result = create_user('홍길동', 30, '서울')
print(result)

print ('현재 가입된 유저 수 :', number_of_people)


