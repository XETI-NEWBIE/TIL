'''
( )( )((( )))
((( )((((( )( )((( )( ))((( ))))))
())
(()
)(
'''
# txt = input()

# top = -1
# stack = [0] * 100

# ans = 1
# for x in txt:
#     if x == '(':    # 여는 괄호 push
#         top += 1
#         stack[top] = x
#     elif x == ')':  # 닫는 괄호인 경우
#         if top == -1:   # 스택이 비어있으면 (여는 괄호가 없으면 )
#             ans = 0
#             break   # for x
#         else:           # 여는 괄호 하나 버림
#             top -= 1    # pop
# if top != -1:   # 여는 괄호가 남아있으면
#     ans = 0

# print(ans)

######################################################

txt = input()
# 스택 생성
top=-1
stack=[0]*100
ans='OK'

for x in txt:
    if x=='(':
        top+=1
        stack[top]='('
    elif x == ')':
        if top== -1:     #여는 괄호가 없으면 오류
            ans = 'Error'
            break       # for x
        else:           #여는 괄호가 있으면 pop
            top-= -1
            # 괄호가 여러 종류면 이 부분에서 비교
if top != -1:
    ans='ERROR'
print(ans) 

    # 비교작업이 필요하면?
    # if stack[top+1] == '(' and x != ')':
    #     break
    # elif stack[top+1] == '{' and x ==:

    # [] 나 {} 가 추가되면? ==> 짝이 맞는지 확인하는 조건문 필요
    # if x == ')':
        # if top == -1 or stack[top] != '(':
            # ans='Error'
            # break
        # top -= 1
# top = -1 ===> stack을 아예 비워버리는 명령
# top -= 1 ===> stack에서 하나씩 꺼내야하는 상황에 적용 가

'''
1. 괄호가 아니면 버림
2. 여는 괄호 => push
3. 닫는 괄호 
    (1) stack에 남아있는 경우 => pop()
    (2) stack에 남아있지 않는 경우 => Error
4. 끝난 후 stack에 남아있으면 오류

'''