# # a=float(input())
# # b=float(input())
# # c=float(input())

# # print(f'{a:.3f}\n{b:.3f}\n{c:.3f}')

# a,b = map(int,input().split())
# c=int(input())
# print(a,b,c, end=" ")

a=float(input())
if a>=1.0:
    print("High")
elif a>=0.5:
    print("Middle")
else:
    print("Low")