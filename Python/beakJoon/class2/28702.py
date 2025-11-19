hint = []
for i in range(3):
    user = input()
    try:
        value = int(user)
    except ValueError:
        value = user
    hint.append(value)
for i in range(3):
    if type(hint[i]) == int:
        hint.append(hint[i]+3-i)
        break
if (hint[3] % 15 == 0):
    hint[3] = "FizzBuzz"
elif(hint[3]% 5 == 0):
    hint[3] = "Buzz"
elif(hint[3]%3 == 0):
    hint[3] = "Fizz"
print(hint[3])



