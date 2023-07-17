import math

x , y, w, h = map(int,input().split())
x_min = x if x <= (w-x) else (w-x)
y_min = y if y <= (h-y) else (h-y)
print(x_min if x_min <= y_min else y_min)