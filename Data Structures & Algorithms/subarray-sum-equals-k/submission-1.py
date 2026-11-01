class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_map = {0:1}

        current_sum=0
        res=0

        for num in nums:
            current_sum += num
            complement = current_sum-k
            if complement in prefix_map:
                res+=prefix_map[complement]

            prefix_map[current_sum] =  prefix_map.get(current_sum, 0) + 1
        return res