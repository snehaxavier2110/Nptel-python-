def binarysearch(arr,element):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        guess=arr[mid]
        if guess == element:
            return mid
        if guess < element :
            low = mid+1
        else:
            high = mid-1
    return None
            
l=[1,3,5,7,9]
print(binarysearch(l,5))
print(binarysearch(l,10))            
        