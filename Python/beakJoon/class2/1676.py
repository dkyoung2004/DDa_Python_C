a = int(input())
multiple = 1
count = 0
for i in range(1,a+1):
    multiple *= i
text = list(str(multiple))
#6자리 리스트 
# 5부터 0까지 -1만큼씩 감
# 6-6
# 6-4
for j in range(len(text)-1,-1,-1):
    if text[j] == '0':
        count +=1
    else:
        print(count)
        break
        

    
