class Solution:
    def search(self, nums: List[int], target: int) -> int:
        result = -1
        l,r = 0, len(nums)-1

        while l <= r:
            m = (l+r) // 2
            if target == nums[m]:
                result = m

            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else: 
                    r = m - 1
            else:
                if nums[m] < nums[r]:
                    if target < nums[m] or target > nums[r]:
                        r = m - 1
                    else:
                        l = m + 1
        return result



        