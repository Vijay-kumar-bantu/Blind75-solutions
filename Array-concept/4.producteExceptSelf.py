"""
Medium category
Leetcode link: https://leetcode.com/problems/product-of-array-except-self/
"""


def productExceptSelf(nums: list[int]) -> list[int]:
        ans = []
        pre = 1
        post = 1
        l = len(nums)

        #Here we are calculating prefix products
        for i in range(l):
            ans.append(pre)
            pre = pre*nums[i]
            
        
        #Here we are calculating postfix products
        for i in range(l-1,-1,-1):
            ans[i] = post*ans[i]
            post = post*nums[i]
            
            

        return ans


#Example
nums = [1,2,3,4]

#output should be [24,12,8,6] for above example
print(productExceptSelf(nums))