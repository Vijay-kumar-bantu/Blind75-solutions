"""
Medium category
leetcode link: https://leetcode.com/problems/maximum-product-subarray/
"""


def maxProduct(nums: list[int]) -> int:
        maxProd = nums[0]
        prefix = 1
        suffix = 1
        l = len(nums)

        for i in range(l):
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1
            
            prefix = prefix * nums[i]
            suffix = suffix * nums[l-i-1]

            maxProd = max(maxProd,max(prefix,suffix))
                
        
        return maxProd


#Example
nums = [2,3,-2,4]

#output should be 6 for above example
print(maxProduct(nums))