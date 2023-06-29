N = int(input())
count = 1
N_var = N
horse = (int(N_var/10) + (N_var%10))
N_var = (((N_var%10)*10)+(horse%10))
while(N_var != N):
    horse = (int(N_var/10) + (N_var%10))
    N_var = (((N_var%10)*10)+(horse%10))
    count+=1
print(count)