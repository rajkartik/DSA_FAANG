def ternary(arr,target):
    l=0
    r=len(arr)-1
   
    while l<=r:
        mid1=l+(r-l)//3
        mid2=r-(r-l)//3
        if arr[mid1]==target:
            return mid1
        if arr[mid2]==target:
            return mid2
        elif arr[mid1]<target and arr[mid2]>target:
            l=mid1+1
            r=mid2-1
        
        elif arr[mid1]>target:
            print("shfgj")
            r=mid1-1
        else:
            print("shfgj")
            l=mid2+1
        
    return False
print(ternary([3,23,56,86,99,101,725],725))