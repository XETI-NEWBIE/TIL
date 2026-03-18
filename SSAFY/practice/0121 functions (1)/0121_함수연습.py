# Lv.1 
def my_multi(number_1, number_2):
    return number_1 * number_2
# my_multi(2, 3) 결과 : 6
# 함수를 수정하고 호출 결과를 result_1 변수에 할당하여 출력하시오.
result_1 = my_multi(2, 3)
print(result_1)

def is_negative(number):
    return number <= 0
"""
boolean 함수의 경우 
def 함수명 (함수인자)
return (함수인자(를 활용한 조건식)) 걸어준 다음에
result~ 출력값 = 함수명 (함수인자)
print(result~)도 잊지 말자
"""
result_2 = is_negative(3)
print(result_2)

# is_negative(3) 결과 : False
# 함수를 수정하고 호출 결과를 result_2 변수에 할당하여 출력하시오.

def default_arg_func(default="기본 값"):
    return default

result_3 = default_arg_func()
result_4 = default_arg_func('다른 값')

print(result_3)
print(result_4)

