"""
Easy category
leetcode link: https://leetcode.com/problems/contains-duplicate/
"""

def containsDuplicate(nums: list[int]) -> bool:
        #creating the hashset to store the seen values
        hashSet = set()

        for i in nums:
            #if value is already seen then return true
            if i in hashSet:
                return True
            
            #if values is not seen, then add it to seen map
            hashSet.add(i)
        return False

#Example
nums = [1,2,3,1]

#Output should be True for above example
print(containsDuplicate(nums))