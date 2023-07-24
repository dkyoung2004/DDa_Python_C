arr = [3,7,2,5,1,4]


def Bubble_Sort(array):

    size = len(array)
    arr = array
    for i in range(0,size):
        print(arr)
        for j in range(1,size-i):
            if(arr[j-1]>arr[j]):
                arr[j] , arr[j-1] = arr[j-1] ,arr[j]


def Selection_Sort(array):
    
    for i in range(0,len(array)):
        min_num = array[i]
        location = i
        for j in range(i,len(array)):#최솟값 탐색
            if(array[j]<min_num):
                min_num = array[j]
                location = j
        array[location],array[i] = array[i],array[location]
        print(array)
    
    return array

def Insertion_Sort(array):

    for i in range(1,len(array)):
        for j in range(1,i+1):
            if(array[i-j] > array[i-j+1]):
               array[i-j+1] ,array[i-j]= array[i-j],array[i-j+1]
            else:
                break
        print(array)

#def Quick_Sort():

        