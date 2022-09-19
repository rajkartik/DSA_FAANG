def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1]= arr[j+1],arr[j]
    return arr
print(bubble_sort([5,3,8,9,0,2,1]))

def selection_sort(arr):
    
    k=0
    for i in range(len(arr)):
        min1=i
        for j in range(i,len(arr)):
            if arr[j]< arr[min1]:
                min1=j
        k+=1
        arr[i],arr[min1]=arr[min1],arr[i]
        
    print(k)
    return arr
        

print(selection_sort([5,3,8,9,0,2,1]))