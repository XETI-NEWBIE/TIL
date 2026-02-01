# a=7
# b=23
# c=30

# # print(a,b,sep="+", end="=")
# # print(c, sep=" ")

# print(f'{a} + {b} = {c}')

""""""
# 추= 13
# 중력= 0.165

# print(f'{추} * {중력:.6f} = ', end="")
# print(f'{(추 * 중력):6f}')

# N = int(input())
# 1<=N<=1000 
# print("Your score is",N,"point.")


# a = int(input())
# a += 2

# print(a)

""""""
# N=float(input())
# 0<=N<=50

# print(f'{N:.2f}')

# a=float(input())
# b=float(input())
# c=float(input())

# print(f'{a:.3f}')
# print(f'{b:.3f}')
# print(f'{c:.3f}')

""""""
# a = int(input())
# b = int(input())

# 1<=a,b<=100

# a, b = b, a
# print(a,b, sep=" ")

# a=int(input())
# b=int(input())

# a = int(input())
# b = int(input())

# a,b=map(int,input().split())
# 1<=a,b<=100
# a,b=b,a

# print(a,b)

""""""
# A,B=map(int,input().split())
# 1<=A,B<=100
# print(A,B,A+B)

# A,B=map(int,input().split())
# 1<=A,B<=100
# sum=A+B
# average=sum/2

# print(sum, average, sep=" ")

""""""
# a,b,c=map(int,input().split())
# 1<=a,b,c<=100
# sum=a+b+c
# average=(a+b+c)/3


# print(sum)
# print(int(average))
# print(int(sum-average))

'''
# 변수 선언, 입력
inp = input()
arr = inp.split()
a = int(arr[0])
b = int(arr[1])
c = int(arr[2])

# 출력
print(a + b + c)
print((a + b + c) // 3)
print((a + b + c) - (a + b + c) // 3)
'''

# N=int(input())

# if N>0:
#     print(N)
# else:
#     print(N,'minus', sep="\n")

# A=int(input().split())
# B=int(input().split())


# A,B=map(int, input().split())

# print(int(A>=B))
# print(int(A>B))
# print(int(B>=A))
# print(int(B>A))
# print(int(A==B))
# print(int(A!=B))

""""""
# N = int(input())

# if N>=80:
#     print("pass")
# else:
#     print(f'{(80-N)} more score')

# a,b=map(int,input().split())

# if a>b:
#     print(a*b)
# else:
#     print(b//a)

""""""
# A,B=map(int,input().split())

# if A<B:
#     print(1, sep=" ", end=" ")
# else:
#     print(0,sep=" ",  end=" ")

# if A==B:
#     print(1,sep=" ", end=" ")
# else:
#     print(0,sep=" ", end=" ") 

""""""
# N = int(input())
# -200<=N<=200

# if N<0:
#     print("ice")
# elif N>=100:
#     print("vapor")
# else:
#     print("water")

""""""
# book= 3000
# mask = 1000

# n=int(input())
# 0<=n<=10000

# if n>=3000:
#     print("book")
# elif n>=1000:
#     print("mask")
# elif n<1000:
#     print("no")

""""""
# A>=90
# B>=80
# C>=70
# D>=60
# F<60

# N=int(input())
# 0<=N<=100

# if N>=90:
#     print("A")
# elif N>=80:
#     print("B")
# elif N>=70:
#     print("C")
# elif N>=60:
#     print("D")
# else:
#     print("F")

""""""
# for i in range(8):
#     print(f'{"G"}', end="")

# N = str(input())
# for i in range(8):
#     print(f'{N}', end="")

""""""
# A,N = map(int, input().split())
# 1<=A,N<=10

# for i in range(N):
#     print(A+N)
#     A+=N

""""""
# for i in range(5,18):
#     print(i)
""""""
# N=int(input())
# 1<=N<=100

# for i in range(1,6):
#     print(N*i, end=" ")

''''''
# A,B = map(int, input().split())

# # 1<=A,B<=100

# for i in range(B,A-1,-1):
#     print(i, end=" ")

''''''
# N, M = map(int, input().split())

# while N > 0:
#     print(N)
#     N//=M
''''''
# a_math, a_english = map(int, input().split())
# b_math, b_english = map(int, input().split())

# if (a_math) > (b_math) and (a_english) >(b_english):
#     print(1)
# else:
#     print(0)
''''''
# a = int(input())

# if a%13==0 or a%19==0:
#     print(True)
# else:
#     print(False)
''''''

# N=int(input())

# if (N%2==1 and N%3==0) or (N%2==0 and N%5==0):
#     print("true")
# else:
#     print("false")

''''''

# gender = int(input())
# age = int(input())

# man = 0
# woman = 1

# if gender == man:
#     if age>=19:
#         print("MAN")
#     else:
#         print("BOY")
# elif gender == woman:
#     if age>=19:
#         print("WOMAN")
#     else:
#         print("GIRL")
''''''

# Y=int(input())

# Leap = "true"
# Common = "false"

# # if Y%4==0:
# #     if Y%100==0 and Y%400!=0:
# #         print(Common)
# #     print(Leap)
# # else:
# #     print(Common)

# if Y%4==0 and Y%100==0 and Y%400!=0:
#     print(Common)
# elif Y%4==0:
#     print(Leap)
# else:
#     print(Common)

'''
# 윤년, 평년 예시 코드
# 변수 선언, 입력
y = int(input())

# 출력
if y % 4 == 0:
	if y % 100 == 0:
		if y % 400 == 0:
			print("true")
		else:
			print("false")
	else:
		print("true")
else:
	print("false")

'''

# A=int(input().split())
# B=int(input().split())
# C=int(input().split())

# A,B,C=map(int, input().split())

# if (A<B<C) or (C<B<A):
#     print(B)
# elif (B<A<C) or (C<A<B):
#     print(A)
# elif (A<C<B) or (B<C<A):
#     print(C)
# else:
#     print(None)

# 중앙값 예시 코드 
# # 변수 선언 및 입력
# inp = input()
# arr = inp.split()
# a = int(arr[0])
# b = int(arr[1])
# c = int(arr[2])

# # 출력
# if a > b:
#     if c > a:
#         # a > b, c > a 일때 (c > a > b)
#         print(a)
#     # a > b, a > c 일때 (a가 가장 크고, b와 c중 더 큰 수가 중앙값)
#     elif b > c:
#         print(b)
#     else:
#         print(c)
# else:
#     if c > b:
#         # b > a, c > b 일때 (c > b > a)
#         print(b)
#     # b > a, b > c 일때 (b가 가장 크고, a와 c중 더 큰 수가 중앙값)
#     elif a > c:
#         print(a)
#     else:
#         print(c)

''''''
# A = [3,1,4,5,9]

# print(A[1]+A[3]+A[4])

''''''

# num = list(map(str, input().split()))
# num.reverse()

# for i in num:
#     print(i, end="")

''''''

# 1차원배열 응용? ... 개헷갈리네 슬슬

# _=input()
# N = map(int, input().split())
# num=[]
    
# for i in N:
#     num.append(i**2)

# print(*num, end="")

''''''
# 줏같은 1차원배열.......일의 자리 배열
# 피보나치 수열 응용한듯..
# 괄호 빼먹지 말고 input(), split() 
# for_in ~ 유용하게 써먹고
# 반드시 어디에 뭘 담고 어떤걸 출력해야하는지 잘 고민해보자

# pivot = list(map(int, input().split()))

# for _ in range(8):
#     num = pivot[-1]+pivot[-2]
#     num = num % 10
#     pivot.append(num)
# # num에서 추가하고 계산된 값을 pivot에 넣어 출력한다
# print(*pivot)