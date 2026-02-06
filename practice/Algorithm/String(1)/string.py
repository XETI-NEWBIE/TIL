#
# N = int(input())
# text = [input() for _ in range(N)]
# print(text)
# print(text[0][2])

    N=int(input())
    text=[list(input())) for _ in range(N)]
    ans = 'No'
    for i in range(N):
        for j in range(N):
            if text[i][j] == 'Z':
                ans = 'YES'
                break     # for j
        if ans == 'YES':
            break # for i
print(ans)

cnt = 0
for i in range(N):
    for i in range(N):
        for j in range(N):
            if text[i][j] == '#':
                cnt += 1
print(cnt)

N=int(input())
text = [input() for _ in range(N)]
pat = ['AB','CD']
ans = 'No'

#AB/CD 패턴 찾기
for i in range(N-1):            # 패턴 기준 i, j
    for j in range(N-1):
        for p in range(2):      # 패턴 내부 인덱스
            for q in range(2):
                if text[i+p][j+q] != pat[p][q]:
                    cnt += 1
        if cnt == 4:
            ans = 'YES'
            # return 'YES'
print(ans)






























