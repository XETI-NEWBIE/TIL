# ############## 주의 ##############
# # 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# # 제한 내장 함수: map, max, sum
# # 기본 점수 (9점): 제한 내장 함수를 사용한 해결
# # 가산점(+3점): 제한 내장 함수 없이 직접 구현 (총 12점)

# def sum_row_maximums(matrix):
#     total_sum = 0 # 각 줄의 최대값들을 다 더할 변수
#     # matrixc의 행을 뽑아옴 ~~~~~~~~
#     for row in matrix:
#         # 일단 맨 앞의 숫자를 이 줄의 최대값이라고 가정
#         max_val = row[0]
        
#         # 그 줄의 숫자들을 하나씩 비교
#         for num in row:
#             if num > max_val:  # 현재 알고 있는 최대값보다 더 큰 수가 나타나면?
#                 max_val = num  # 최대값 갱신
        
#         # 찾은 최대값을 전체 합계에 더하기
#         total_sum += max_val
        
#     return total_sum
    # 여기에 코드를 작성하여 함수를 완성합니다.

# # 추가 테스트를 위한 코드 작성 가능
# # 예) print(함수명(인자))

# def sum_row_maximums(matrix):
#     total_sum = 0
#     for row in matrix:
#         row.sort(reverse=True)
#         total_sum+=row[0]
    
#     return total_sum

def sum_row_maximums(matrix):
    total_sum = 0
    for row in matrix:
        row.sort(reverse=True)
        total_sum+=row[0]
    return total_sum

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다.
############## 테스트 코드 삭제 금지 #################
print(sum_row_maximums([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) # 18
print(sum_row_maximums([[-1, -2, -3], [-10, -5, -1], [-100, -200, -300]])) # -102
print(sum_row_maximums([[5]])) # 5
#####################################################


# def sum_row_maximums(matrix):
#     total_sum = 0
    
#     for row in matrix:
#         # 1. 줄(row)을 큰 순서대로 정렬합니다.
#         # reverse=True를 쓰면 [9, 8, 7...] 처럼 큰 놈이 앞으로 와요.
#         row.sort(reverse=True)
        
#         # 2. 맨 앞에 있는 놈(최대값)을 가져와서 더합니다.
#         total_sum += row[0]
        
#     return total_sum


# def sum_row_maximums(matrix):
#     total_sum = 0
#     for row in matrix:
#         # 파이썬 내장 함수 max()를 써서 바로 최대값을 찾습니다.
#         total_sum += max(row)
#     return total_sum