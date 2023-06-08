literate = int(input())
for i in range(0,literate):
    streak = 0
    total = 0
    Ox = input()
    for j in Ox:
        if j == "O":
            streak +=1
            total += streak
        else:
            streak = 0
    print(total)

