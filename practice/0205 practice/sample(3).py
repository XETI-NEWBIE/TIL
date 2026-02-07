# A,B=map(int,input().split())

# count=0

# for i in range(A,B+1):
#     if i %2 ==0:
#         count+=1
#     else:
#         continue
# print(i)
''''''
# [ 정답 코드 ]
# A,B = map(int,input().split())
# count=0
# for i in range(A,B+1):
#     if i%2==0:
#         count += i
#     else:
#         continue
# print(count)

#####################

# 10개의 수 => 3의 배수의 개수와 5의 배수의 개수를 출력
# a,b,c,d,e,f,g,h,i,j=map(int, input().split())

# total=0
# count=0

# for i in range(a,j+1):
#     if i%3==0:
#         total+=1
#         count+=1
#     elif i%5==0:
#         total+=1
#         count+=1

# print(count)

# ❌ 잘못된 부분 분석
# 1. 입력 방식의 오해:
# 문제 사진을 보면 숫자가 한 줄에 하나씩 총 10줄에 걸쳐 들어옵니다.
# 하지만 채원님은 map(int, input().split())을 써서 한 줄에 10개가 다 들어오는 것으로 처리하셨어요. 이러면 입력 단계에서 에러가 납니다.
# 2. 범위(range)의 오해:
# range(a, j+1)라고 하셨는데, 이건 첫 번째 숫자와 마지막 숫자 사이의 모든 수를 검사하겠다는 뜻이에요.
# 문제는 입력받은 그 10개의 숫자 각각이 3이나 5의 배수인지 확인하라는 것입니다.
# 3. 카운팅 로직:
# 3의 배수 개수와 5의 배수 개수를 따로 구해서 공백을 두고 출력해야 합니다.
# 지금처럼 한 바구니(count)에 다 담으면 안 돼요.

cnt_3 = 0
cnt_5 = 0

for i in range(10):
    num = int(input())
    if num%3==0:
        cnt_3+=1
    if num%5==0:
        cnt_5+=1
print(cnt_3, cnt_5)