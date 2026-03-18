#1 Time to Time
# 
# a, b, c, d = map(int, input().split())

#2시 5분에서 시작하여 4시 1분까지 소요되는 시간
#120분- 4분 = 116분 소요
# (4*60)+1 - (2*60)+(5*1) = 241분 - (120분+5분) = 116분

# num_1 = (c*60)+(d*1)
# num_2 = (a*60)+(b*1)

# result = num_1 - num_2

# print(result)


# 2
# Date to Date 

m1,d1,m2,d2 = map(int, input().split())

num_of_days = [0, 31,28,31,30,31,30,31,31,30,31,30,31]

def total_days(m,d):
    total = 0
    for i in range(1,m):
        total += num_of_days[i]
    total += d
    return total

all_days = total_days(m2,d2) - total_days(m1,d1) + 1

print(all_days)
