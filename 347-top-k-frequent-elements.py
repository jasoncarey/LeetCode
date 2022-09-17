# Top K Frequent Elements
# ----------
# Medium
# Array, Heap

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        h = []
        d = {}
        res = []
        
        # get frequency dictionary
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        
        for i, val in d.items():
            # turn minheap into maxheap
            heappush(h, (-val, i))
            
        for j in range(0, k):
            val, i = heappop(h)
            res.append(i)
        return res
            