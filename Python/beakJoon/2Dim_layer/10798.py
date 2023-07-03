array = []
length = []
for i in range(0,5):
    word = input()
    array.append(word)
    length.append(len(word))
for i in range(max(length)):
    for j in range(0,5):
        if (i < length[j]):
            print(array[j][i],end="")