############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.
# 제한 Python 내장 함수: reversed, list.reverse
# 기본 점수 (9점): 제한 내장 함수를 사용하여 해결
# 가산점(+3점): 제한 내장 함수 없이 직접 구현 (총 12점)
'''
리스트 뒤집기 : 기존 리스트의 순서를 역순(reverse)로 재배치할 수 있는가?
'''
def reverse_list(visited_items):
    reversed_result = [] # 결과를 담을 빈 리스트 생성
    
    # 1. 일단 슬라이싱으로 뒤집힌 가방을 하나 만들어 버린다!
    reversed_bag = visited_items[::-1]
    
    # 2. 뒤집힌 보따리에서 하나씩 꺼내서 내 바구니에 담습니다
    for item in reversed_bag:
        reversed_result.append(item)
        
    return reversed_result

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

def reverse_list(visited_items):
    reversed_bag= []
    reverseds_list=visited_items[::-1]
    
    for item in reverseds_list:
        reversed_bag.append(item)
    
    return reversed_bag

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(reverse_list([1, 2, 3, 4, 5]))  # [5, 4, 3, 2, 1]
print(reverse_list(['A', 'B', 'C']))  # ['C', 'B', 'A']
#####################################################

# #1
# def reverse_list(visited_items):
#     reversed_result = []
    
#     # 1. len()을 못 쓰니까 일단 개수를 먼저 셉니다 (가산점 조건!)
#     count = 0
#     for item in visited_items:
#         count += 1
    
#     # 2. 뒤에서부터 거꾸로 숫자를 세며 아이템을 꺼냅니다
#     # 예: 인덱스 4, 3, 2, 1, 0 순서로!
#     for i in range(count - 1, -1, -1):
#         reversed_result.append(visited_items[i])
        
#     return reversed_result


# #2
# def reverse_list(visited_items):
#     # 처음부터 끝까지 가는데, -1칸씩(거꾸로) 가라!
#     return visited_items[::-1]
