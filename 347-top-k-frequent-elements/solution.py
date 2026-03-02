from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for num in nums:
            if num in d:
                d[num] += 1
            else: 
                d[num] = 1
        sorted_d = sorted(d.items(), key=lambda kv: kv[1], reverse=True) # looked up how to do
        result = list()
        for i in range(k):
            result.append(sorted_d[i][0])
        return result