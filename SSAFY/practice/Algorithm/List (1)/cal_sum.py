# n까지의 합을 반환하는 함수를 작성
def calc_sum(n):
    # 총합을 저장할 변수를 선언하여 0으로 초기화
    total = 0
    # 숫자 1부터 n까지 반복한다.
    # 반복한 숫자를 i에 저장한다.
    for i in range(1, n+1):
        # total에 total + i를 저장한다
        total = total + i
    # total을 반환한다
    return total

# 의사코드 = python code로 대치가 가능한 주석 코드라고도 볼 수 있다.
# 내가 뭘 하겠다~라는 결정을 내리는 것! 주석은 평가때도 필수 ~!!