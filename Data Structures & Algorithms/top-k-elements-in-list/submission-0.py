class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = Counter(nums)
        most_common_tuples = counts.most_common(k)
        return [item[0] for item in most_common_tuples]