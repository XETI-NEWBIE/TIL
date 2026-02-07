############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.

def find_second_largest(numbers):
    # set로 증복 제거에만 써먹어버리고 list로 다시 변신시켜서
    # 순서 index 만들어서 정렬하고 값 꺼내주기 ㅋㅋ
    onlyone_number = list(set(numbers))
    onlyone_number.sort(reverse=True)
    # 두 번째로 큰 값을 반환한다 => index [1] 을 의미
    return onlyone_number[1]


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(find_second_largest([1, 5, 3, 8, 2]))      # 5
print(find_second_largest([10, 10, 20, 5]))      # 10
#####################################################