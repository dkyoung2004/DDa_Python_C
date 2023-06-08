a = ""
a = str(input())
a = a.upper()

var = 0
highest = 0
highest_string = ""

for i in range(65,91):
    var = a.count(chr(i))
    if var > highest:
        highest = var
        highest_string = chr(i)
    elif var == highest:
        highest_string = "?"
print(highest_string)