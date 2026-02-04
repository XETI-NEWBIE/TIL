############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 제한 내장 함수: sum, len, map
# 기본 점수 (9점): 제한 내장 함수를 사용한 해결
# 가산점(+3점): 제한 내장 함수 없이 직접 구현 (총 12점)

'''
2차원 리스트 순회 : 리스트 안의 리스트를 끝까지 다 훑으면서 조건에 맞는 값을 찾아낼 수 있는가?

이중 반복문 (for) 안에 for을 써서 복잡한 구조의 데이터를 훑는 능력을 판단
0인 칸은 무시하고 실제 물건이 있는 칸만 세는 예외 처리가 필수적

'''
def count_total_items(warehouse): 
    total_count = 0  # 전체 물건 개수

# row(행)을 한 줄 쫙 훑고 나서 => 해당 row(행)에 있는 item을 하나씩 줍줍
# [1,0,2] 한 번 돌아주고 ㅋㅋ => 1, 0, 2 하나씩 뽑아와서 확인... 확인..

    for row in warehouse:       # 창고의 한 줄씩 꺼내서 
        for item in row:        # 그 줄에 있는 칸들을 하나씩 확인
            if item != 0:       # 빈 칸(0)이 아니면?
                total_count += 1  # 개수 세기
                
    return total_count
   
# 전체 물건 꺼내기 => 실제 물품이 있는 칸 꺼내기 

def count_total_items(warehouse):
    total_count = 0
    for space in warehouse:
        for items in space:
            if items!=0:
                total_count += 1
# return total_count

def count_total_items(warehouse):
    total_count=0
    
    for space in warehouse:
        for items in space:
            if items != 0:
                total_count+=1
    return total_count

    # 여기에 코드를 작성하여 함수를 완성합니다.

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우
# 모든 책임은 삭제한 본인에게 있습니다.
############## 테스트 코드 삭제 금지 #################
print(count_total_items([[1, 0, 2], [3, 4, 5], [0]]))    # 5
print(count_total_items([[0, 0], [0], [30, 40]]))    # 2

#####################################################