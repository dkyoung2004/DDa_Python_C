arr = []
max_num = 0
max_index = 0



# 리스트 선언
for _ in range(10):
    arr.append(int(input()))

#arr에 입력값을 하나씩 저장
for value in arr: #arr(리스트)를 0번째 자리부터 마지막까지 가면서, 각 자리에 있는 값을 value에 저장
    if max_num < value:
        max_num = value
        max_index = arr.index(value)
        
    


