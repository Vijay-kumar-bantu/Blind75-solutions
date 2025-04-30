




def findInArray(arr:list[int],target:int)->int:
    low = 0
    high = len(arr)-1

    while high>=low:
        mid = (low+high)//2

        if(arr[mid] == target):
            return mid
        
        if(arr[mid]>target and arr[mid]>arr[high]):
            low = mid + 1
        else:
            high = mid -1

    return -1 

#example
arr = [1,3]
target = 3

print(findInArray(arr,target))

