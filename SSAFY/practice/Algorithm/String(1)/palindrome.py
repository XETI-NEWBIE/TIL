
import sys
sys.stdin = open("palindrome.txt", "r")

T = int(input())
for test_case in range(1, T + 1):

# 거꾸로 읽어도 제대로 읽은 것 같은 문장/단어 = 회문
# 3<= word_length <=10
# # 회문은 문자열길이/2 = n이라면 int(n)만큼 반복해주면 됨
# for i: 0 -> len(txt) / 2 - 1
#     if txt[i] != txt[len(txt) - 1 - i]:
#         return False
#     return True
# print(f'#{t}')

# def palindrome(word, word_length):
    word = input()
    N = len(word)
### circle 변수 설정
# 변수 설정 값을 뭐 어떻게 줘야하나?
# if문에서 N-1-j를 해주므로...
    circle = 1
# 반드시 circle[]이라고 하면 N-1-i
# 와 또 변수[리스트]꼴을 못 풀겠다 어떻게 설정하지???????
# circle로 N-1-i 를 감싸준다 ㅎㅎ
    for i in range(N//2):
        # circle[N-1-i] 가 아니라, word[N-1-i] 라는 것을 기억할 것
        if word[i] != word[N - 1 - i]:
            circle = 0
        break


    print(f'#{test_case} {circle}', sep=" ")
