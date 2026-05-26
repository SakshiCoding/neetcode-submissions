class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cons = set(nums)
        seq = 1
        longest = 0
        for num in cons:
            if (num-1) not in cons:
                seq = 1
                while (num + seq) in cons:
                    seq += 1
                longest = max(seq, longest)
        return longest
                



        