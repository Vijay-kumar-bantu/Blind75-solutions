
'''
Medium category
leetcode link : https://leetcode.com/problems/find-minimum-in-rotated-sorted-array
Note: this should be solve in O(logn) time
Notes: check if half of array is sorted in order to find pivot, arr is guaranteed to be in at most two sorted subarrays
'''


#Solution  

def findMin(arr:list[int])->int:
    minimum = float("inf")
    low = 0
    high = len(arr)-1

    while(high>low):
        mid = (high+low)//2

        if(arr[mid]<minimum):
            minimum = arr[mid]
        
        if(arr[mid]<=arr[high]):
            high = mid - 1
        else:
            low = mid + 1
    
    return minimum


#example problem
arr = [3,4,5,1,2]

#answer should be 1
print(findMin(arr))
