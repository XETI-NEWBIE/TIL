
# 마지막만 쉼표 빼고 싶을 땐 if문 활용 (조건 잘 쓰기 ;;;;;;)
# N=int(input())
# for i in range(1, N+1):
#     for j in range(1, N+1):
#         if j==N: 
#             print(f'{i} * {j} = {i*j}', end=" ")
#         else:
#             print(f'{i} * {j} = {i*j},', end=" ")
#     print()
    
# 숫자 피라미드
# range 범위 생각 좀 잘해보기....  안쪽 for문은 바깥쪽 for문 고려해서 써보기.... 내머리로좀풀어봐라 선종오빠가거의풀어줌 ;;;;
N = int(input())
for i in range(1, N+1):
    for j in range(1,i+1):
        print(i, end=" ")
    print()
    
# 1번줄이 1이면 1개 2번줄이 2이면 2개 3버줄이 3이면 3개 
# i가 range에서 1이면 1개... i==N아닌가? 