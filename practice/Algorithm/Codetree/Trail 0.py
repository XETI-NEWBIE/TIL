
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
# N = int(input())
# for i in range(1, N+1):
#     for j in range(1,i+1):
#         print(i, end=" ")
#     print()
    
# 1번줄이 1이면 1개 2번줄이 2이면 2개 3버줄이 3이면 3개 
# i가 range에서 1이면 1개... i==N아닌가? 

# # 약수 출력하기

# n=12

# for i in range(1, n+1):
#     if n%i==0:
#         print(i)


# # 특정 수의 약수 찾기 5번 반복
# for _ in range(5):
#     n = int(input("약수를 찾을 수를 입력하세요 :"))
    
#     # 단일 for문으로 n의 약수를 찾고 출력
#     for i in range(1, n+1):
#         if n%i ==0:
#             print(i, end=' ')
#     print()

# 여러 줄에 거쳐 입력값 받기
# 짝수의 합 N번 구하기

# 개망한코드
# N = int(input())

# for _ in range(N+1):
#     a, b = map(int, (input().split()))
#     if b%a==0:   
#         for _ in range(b):
#             print(a//b==0, end=' ')
#     else:
#         break

# # 정답코드
# N = int(input())
# # N+1가 아니라 N번만큼 루프 반복 (임시변수는 _ 처리(횟수만 중요))
# for _ in range(N):
#     a,b = map(int, input().split())
#     # '합' 이므로 카운티 변수 필수
#     total_sum=0
#     # a부터 b까지 숫자를 하나씩 꺼내준다
#     for num in range(a,b+1):
#         # 꺼낸 숫자가 짝수라면~
#         if  num%2==0:
#             total_sum+=num
    
#     print(total_sum)   

# 약수가 세 개인 수
# a, b = list(map(int, input().split()))
# total_count = 0

# for num in range(a,b+1):
#     # 언제나 그렇듯 if문 조건 설정 문제
#     # int != iterable => 숫자는 for문에 넣어서 하나씩 꺼낼 수 없음
#     # Zerodivisonerror : range는 0부터 시작하기 때문에 0으로 나눌라다가 에러뜬거임
#     # num%i ====> 1, num+1 로 수정
#     # 해당 숫자(num)의 약수가 몇 개인지 셀 변수를 설정해줘야 한다 (숫자가 바뀔 때마다 0으로 초기화) 
#     divisor_count = 0
    
#     for i in range(1, num+1):
#         if num%i==0:
#             divisor_count += 1 # num/i로 딱 나누어 떨어지면 약수 개수 +1 
        
#     if divisor_count == 3:
#         total_count+=1
# # 들여쓰기 중요
# print(total_count)

# # 2중 반복문에서의 변수 사용
# # 
# A = [1, 3, 2]
# B = [4, 1, 0, 2]

# for i in range(3):
#     sum_ab = 0
#     for j in range(4):
#         # A[1] 일 때만 출력
#         # A[1] 은 3이다. 그러므로 B[0~3]을 돌면 3*4 + 3*1 + 3*0 + 3*2 = 12+3+0+6= 21
#         sum_ab += (A[i]*B[j])

#     if i == 1:
#         print(sum_ab)


# 숫자피라미드 2
# 선종오빠 찬스 (count 외부/내부 헷갈림 => 죽어)
# N = int(input())
# count = 0

# for i in range(1,N+1):
#     for j in range(1,i+1):
#         count+=1
#         print(count, end=" ")
#     print()


# # 그냥 머리 터짐
# # 2차원 배열 응용

# array1 = [[1, 2, 3], [4, 5, 6]]
# array2 = [[1 for j in range(3)] for i in range(2)]

# for i in range(2):
#    for j in range(3):
#       print(array1[i][j] + array2[i][j], end=' ')
#    print()

# # 새로운 배열 생성
# # 원본 배열을 2배로 복사하기 (모든 요소를 2배로 복사)

# matrix = [[1,-1],[0,5]]
# rows = 2
# cols = 2

# new_matrix = []
# for i in range(rows):
#     new_row = []
#     for j in range(cols):
#         # 각 요소에 2를 곱하여 새로운 행에 추가
#         new_row.append(matrix[i][j] * 2)
#     new_matrix.append(new_row)
    
# print("새롭게 생성된 배열(new_matrix):")
# for row in new_matrix:
#     print(row)
    
# # 출력
# "새롭게 생성된 배열(new_matrix):"
# [2, -2]
# [0, 10]


# 배열의 값을 3배로 !
# arr = [list(map(int, input().split())) for _ in range(3)]
# # arr = int(input)
# rows = 3
# cols = 3

# for i in range(rows):
#     for j in range(cols):
#         print(arr[i][j]*3, end=" ")
#     print()
    
# # 두 배열의 곱
# 망한 코드 ( 내코드 )
# arr_1 = [list(map(int, input().split())) for _ in range(3)]
# arr_2 = [list(map(int, input().split())) for _ in range(3)]

# rows = 3
# cols = 3

# for i in range(1, 4):
#     for j in range(1, 4):
#        result = [ i * j for i, j in zip(arr_1, arr_2)]
#        print(result)
#     print()
    
# # 두 배열의 곱
# # 정답 코드
# arr_1 = [list(map(int, input().split())) for _ in range(3)]
# # 아니 2차원 배열과 배열 사이에 공백이 있네 ;;;;
# # 이럴땐 input() 넣어준다
# input()
# arr_2 = [list(map(int, input().split())) for _ in range(3)]

# #  0번 인덱스부터 2번까지 훑기 (range(3)이면 idx는 0,1,2)
# for i in range(3):
#     for j in range(3):
#         # 같은 위치(i, j)의 숫자끼리 곱해서 출력
#         # 첫번쨰 배열의 (1,1)과 두번째 배열의 (1,1)을 곱하고 싶다면 아래처럼 쓰면 된다. 
#         # 왜 이렇게 직관적이냐
#         print(arr_1[i][j] * arr_2[i][j], end=" ")
#     print() # 한 줄 끝날 때마다 줄바꿈


# 배열의 합

# 개망한 코드
# arr = [list(map(int, input().split())) for _ in range(4)]

# for row in arr:
#     print(sum(arr))

# # 쌰ㅐ갈 !!!!!!!!!!!!! 드디어됏더
# # sum () 를 row에 적용해서 count에 할당하는게 답이었다 !

# arr = [list(map(int, input().split())) for _ in range(4)]
# count = 0

# for row in arr:
#     # for cols in row:
#         # arr에 첫째줄~ 넷째줄의 각 행의 값들을 합하여 각각 출력한다.
#         # arr의 첫 행의 값들을 모두 더하고 ~ 두번째 행의 값들을 모두 더하고 ~ 하는 매우쉬운문제
#         # 첫 행 : arr[0]~arr[3] 까지 
#     count = sum(row)
    
#     print(count)


# # 5의 배수의 개수는?
# # 바로 맞춰버림 ;;;;; 
# arr = [list(map(int, input().split())) for _ in range(4)]
# row = 4
# cols=4

# count=0

# for row in arr:
#     for cols in row:
#         if cols%5==0:
#             count+=1
#     print(count)
    
# 지그재그 단계별 구현
# n = 3
# cnt = 1

# for i in range(n):
#     row=[]
#     # 기본 숫자 배열 생성하기
#     for j in range(n):
#         row.append(cnt)
#         cnt+=1
#     # 짝수 행과 홀수 행 구분하기
#     if i%2 != 0:
#         # i가 홀수인 경우, row배열의 순서를 뒤집어 반대로 출력
#         # 홀수 행은 오른쪽에서 왼쪽으로 수가 감소하는 형태
#         # 현재 행 번호에 따라 정방향 / 역방향으로 출력
#         for j in range(n-1, -1, -1):
#             print(row[j], end=" ")
#     else:
#         for j in range(n):
#             print(row[j], end=" ")
#     print()
    
# # 지그재그 순회
# array = []
# n = row
# m = cols
# for i in range(n):
#     for j in range(m):
#         f(array[i][j + (m-1-2*j) * (i%2)])

# 길이단위 변환하기
# 1피트 = 30.48cm
# 1마일 = 160934cm
# 9.2피트와 1.3마일을 각각 cm로 변환

# ft   =>  cm
# cm => ft * 30.48

# mil/mile  =>  cm
# cm = > mile * 160,934

# a = float(input())
# b = a+1.5
# print(f'{b:.2f}')

##############################################

# N = int(input())

# for i in range(1,6):
#     print(i*N, end=" ")
    
# A,B = map(int, input().split())

# for i in range(B,A-1,-1):
#     print(i, end=" ")\

# N, M = map(int, input().split())

####################################################

# a = int(input())

# # for i in (13,19):
# if a%13==0 or a%19==0:
#     print(bool(1))
# else:
#     print(bool(0))
    
    
# N = int(input())

# if (N%2==1 and N%3==0) or (N%2==0 and N%5==0):
#     print("true")
# else:
#     print("false")

# gender = int(input())
# age = int(input())

# # man = 0
# # woman = 1

# if gender == 0 and age>=19:
#     print("MAN")
# elif gender==1 and age>=19:
#     print("WOMAN")
# elif gender==0 and age<19:
#     print("BOY")
# else:
#     print("GIRL")

# 2011년 11월 11일 2시 5분에서 4시 1분까지

# a, b, c, d = map(int, input().split())

# print((c*60+d)-(a*60+b))



Y = int(input())

if Y%4==0:
    print("true")
if Y%100==0 and Y%400!=0:
    print("false")
else:
    print("false")
# elif Y%4==0 and Y%100==0 and Y%400!=0:
#     print("false")
# else:
#     print("false")