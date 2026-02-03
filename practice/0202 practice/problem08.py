############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.

def find_second_largest(numbers):
    # 1단계: 제일 큰 수(1등) 찾기
    first_max = numbers[0]
    for num in numbers:
        if num > first_max:
            first_max = num
            
    # 2단계: 1등이 아닌 수 중에서 제일 큰 수(2등) 찾기
    # 초기값은 아주 작은 수로 설정하거나 리스트의 첫 값으로 비교 시작
    second_max = -9999999999 
    
    for num in numbers:
        # 1등 숫자가 아니어야 함 (중복 제외 효과)
        if num != first_max:
            # 현재 알고 있는 2등보다 크면 갱신
            if num > second_max:
                second_max = num
                
    return second_max


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(find_second_largest([1, 5, 3, 8, 2]))      # 5
print(find_second_largest([10, 10, 20, 5]))      # 10
#####################################################