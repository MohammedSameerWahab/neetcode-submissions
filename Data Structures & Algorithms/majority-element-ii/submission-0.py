class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        counts = Counter(nums)
        ans=[]

        for item, freq in counts.items():
            if freq>(len(nums)//3):
                ans.append(item)
        return ans