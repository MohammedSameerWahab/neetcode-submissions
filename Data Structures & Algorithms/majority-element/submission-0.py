class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = len(nums)/2
        freq = {}
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i], 0) +1
        for k in freq:
            if freq[k] > m:
                return k