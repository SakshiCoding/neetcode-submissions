class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zeroes = 0
        result = [0] * len(nums)
        for num in nums:
            if num:
                prod *= num
            else:
                zeroes += 1
        if zeroes > 1:
            return [0] *len(nums)
        for i, c in enumerate(nums):
            if zeroes: result[i] = 0 if c else prod
            else: result[i] = prod // c
        return result

        
            

        