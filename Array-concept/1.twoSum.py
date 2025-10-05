"""
Easy category
leetcode link: https://leetcode.com/problems/two-sum/description/
Notes: use hash map to instantly check for difference value, map will add index of last occurrence of a num, don’t use same element twice
"""


#Solution

#the function will return the array of indexes where the sum of values will be equal to the target
def getTwoSum(nums:list[int], target:int)->list[int]:
        #a hashmap where each difference of every index will be stored
        differenceMap = dict()

        for i in range(len(nums)):
            #checking whether the difference is already existed in the map
            if nums[i] in differenceMap.keys():
                #if existed returns the answer
                return [differenceMap[nums[i]],i]
            
            #if not existed adding the difference of index to the map
            differenceMap[target - nums[i]] = i

def testFunction():
    print("Hello world")

#Example
nums = [2,7,11,15]
target = 9

#output should be [0,1] for above example
print(getTwoSum(nums,target))
