# a=7
# b=23
# c=30

# # print(a,b,sep="+", end="=")
# # print(c, sep=" ")

# print(f'{a} + {b} = {c}')


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


# N=float(input())
# 0<=N<=50

# print(f'{N:.2f}')

# a=float(input())
# b=float(input())
# c=float(input())

# print(f'{a:.3f}')
# print(f'{b:.3f}')
# print(f'{c:.3f}')


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

# A,B=map(int,input().split())
# 1<=A,B<=100
# print(A,B,A+B)

# A,B=map(int,input().split())
# 1<=A,B<=100
# sum=A+B
# average=sum/2

# print(sum, average, sep=" ")


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

# A,B=map(int,input().split())

# if A<B:
#     print(1, sep=" ", end=" ")
# else:
#     print(0,sep=" ",  end=" ")

# if A==B:
#     print(1,sep=" ", end=" ")
# else:
#     print(0,sep=" ", end=" ") 

# N = int(input())
# -200<=N<=200

# if N<0:
#     print("ice")
# elif N>=100:
#     print("vapor")
# else:
#     print("water")

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


# A>=90
# B>=80
# C>=70
# D>=60
# F<60

N=int(input())
0<=N<=100

if N>=90:
    print("A")
elif N>=80:
    print("B")
elif N>=70:
    print("C")
elif N>=60:
    print("D")
else:
    print("F")