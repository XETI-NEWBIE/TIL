
# 원형 큐 연습

n=3
cq = [0] * n
front = near = 0

def enqueue(item):
    global rear
    if is_full():
        print("Queue_is_full")
    else:
        # rear값 조정 (q의 크기로 나머지를 구해서 다음 자리로 지정) => new 원소 삽입 자리 지정
        # 마지막 원소 뒤에 새로운 원소 삽입
        # new 원소 인덱스에 해당하는 배열원소 cq[rear]에 item을 저장
        rear = (rear+1)%len(cq)
        cq[rear] = item

def dequeue():
    global front
    if is_empty():
        print("Queue_Empty")
    else:
        # 가장 앞에 있는 원소를 삭제
        # front값 조정하여 삭제 자리 지정 => new front원소 리턴 = 삭제기능수행
        front = (front+1)%len(cq)
        return cq[front]

# 공백 상태 : front ==rear
def is_empty():
    return front==rear
# 포화 상태 : 삽입할 rear의 다음 위치 == 현재 front
def is_full():
    return (rear+1)%len(cq)==front
