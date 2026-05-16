class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Nhash = {}
        for i in nums:
            if i in Nhash:
                Nhash[i] += 1
            else:
                Nhash[i] = 1
        sorted_items = sorted(Nhash.items(), key=lambda x: x[1], reverse=True)
        output = [item[0] for item in sorted_items[:k]]
        return output
