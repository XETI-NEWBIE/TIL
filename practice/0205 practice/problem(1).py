############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 제한 내장 함수:  len, sum
# 기본 점수 (9점): 제한 내장 함수를 사용하여 해결
# 가산점(+3점): 제한 내장 함수 없이 직접 구현 (총 12점)

'''
평균 구하기 
: 리스트 요소의 전체 합을 구하고 개수로 나눌 수 있는가?

=> for문을 통한 누적합 계싼하는 누적합 로직 계산이 필수적
'''

def calculate_avg(temperatures):
    total = 0  # 합계를 담을 그릇
    count = 0  # 개수를 셀 그릇

    # 리스트에 있는 온도를 하나씩 꺼내서
    for temp in temperatures:
        total += temp   # 합계에 더하고
        count += 1   # 개수를 1 증가시킴
    
    # 합계 나누기 개수 = 평균 (실수형 변환)
    return float(total / count)

    # 여기에 코드를 작성하여 함수를 완성합니다.

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(calculate_avg([20, 25, 30, 22, 28]))  # 25.0
print(calculate_avg([10, 10, 10]))          # 10.0
print(calculate_avg([1, 2, 4]))          # 2.3333333333333335
#####################################################

# def calculate_avg(temperatures):
#     total = 0
#     count = 0
#     for temp in temperatures:
#         total += temp # total에 temp(온도 1개)를 더한다
#         count += 1 # 몇 개 더하고 있는지 실시간 누적 카운팅

#     return float(total/count) 


#