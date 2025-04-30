"""
Medium category
leetcode link: https://leetcode.com/problems/maximum-subarray/
"""

def maxSubArray(nums: list[int]) -> int:
        maxsum=nums[0]
        temp=0


        for i in nums:
            if temp<0:
                temp=0
            temp = temp + i
            if temp>maxsum:
                maxsum=temp
            
        return maxsum


#Example
nums = [-2,1,-3,4,-1,2,1,-5,4]

#output should be 6 for above example
print(maxSubArray(nums))