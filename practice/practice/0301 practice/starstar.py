# n=int(input())

# # for i in range(n):
# #     star = n-i
# #     unit = "*" * star + " "
# #     print(unit*star)
# #     "*"*(n-1)

# for i in range(n,0,-1):
#     star = "*" * i + " "
#     print(star*i)

##############

# n=int(input())

# for i in range(n):
#     print("*"*n)
# print()
# for i in range(n):
#     print("*"*n)

# n=int(input())

# for i in range(n):
#     print("*"*i)

#     print()
    
# for i in range(n):
#     print("*"*i)

# n=int(input())

# for i in range(n):
#     print("*"*i)
#     for j in range(i):
#         print("*"*j)

# # 학생 수 입력 받기
# n = int(input())

# # 통과한 학생 수를 셀 변수 초기화
# pass_count = 0

# # 학생 수만큼 반복 처리하기
# for _ in range(n):
#     # 4개의 점수를 리스트로 맵핑
#     scores = list(map(int, input().split()))
    
#     # 4과목의 평균값 구하기
#     avg = sum(scores) / 4
    
#     # 평균이 60점 이상인지 확인
#     if avg >= 60:
#         print("pass")
#         pass_count += 1  # 통과한 인원 추가해주기
#     else:
#         print("fail")

# # 마지막에 총 통과 학생 수 출력!!!
# print(pass_count)


# total = 0
# cnt = 0

# while True:
#     n = int(input())
#     # 20대 범위 벗어나면 즉시 종료
#     if n < 20 or n >= 30:
#         break
    
#     total += n
#     cnt += 1

# # 평균 계산
# print(f"{total / cnt:.2f}")

# # A, B, C, D 진료소에 가는 인원을 저장할 리스트
# results = [0, 0, 0, 0]

# # 3명의 정보를 하나씩 확인
# for _ in range(3):
#     info = input().split()
#     symp = info[0]      # 증상 (Y or N)
#     temp = int(info[1]) # 체온
    
#     # 조건에 맞춰 진료소 분류
#     if symp == 'Y' and temp >= 37:
#         results[0] += 1 # A 진료소
#     elif symp == 'N' and temp >= 37:
#         results[1] += 1 # B 진료소
#     elif symp == 'Y' and temp < 37:
#         results[2] += 1 # C 진료소
#     else:
#         results[3] += 1 # D 진료소

# print(*(results), end="")

# # 만약 A 진료소(results[0])에 2명 이상이면 E 출력
# if results[0] >= 2:
#     print(" E")
# else:
#     print() # 그냥 줄바꿈

# clinic_counts = [0, 0, 0, 0]

# # 3명의 정보를 순서대로 입력받아 처리
# for _ in range(3):
#     info = input().split()
#     symptoms = info[0]      
#     temperature = int(info[1]) 
    
#     # 분류 규칙 적용
#     if symptoms == 'Y' and temperature >= 37:
#         clinic_counts[0] += 1 # A 
#     elif symptoms == 'N' and temperature >= 37:
#         clinic_counts[1] += 1 # B
#     elif symptoms == 'Y' and temperature < 37:
#         clinic_counts[2] += 1 # C 
#         clinic_counts[3] += 1 # D

# # 진료소 인원 출력 
# print(*(clinic_counts), end="")

# # 위급상황 판단 => A로 가는 사람이 2명 이상일 때
# if clinic_counts[0] >= 2:
#     print(" E")
# else:
#     print() # 줄바꿈만 !

n, q = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(q):
    query = list(map(int, input().split()))
    type_num = query[0]
    
    if type_num == 1:
        # a번째 원소 출력
        a = query[1]
        print(arr[a-1])
        
    elif type_num == 2:
        # 값이 b인 원소 중 가장 작은 인덱스 찾기
        b = query[1]
        result = 0
        for i in range(n):
            if arr[i] == b:
                result = i + 1 # 1번째부터 세므로 +1 해주기
                break
        print(result) # 없으면 0 출력
        
    elif type_num == 3:
        # s번째부터 e번째까지 원소 출력
        s, e = query[1], query[2]
        # 리스트 슬라이싱 활용 
        print(*(arr[s-1:e]))


# 연속부분수열일까 문제 
# 문자열 파트 복습
