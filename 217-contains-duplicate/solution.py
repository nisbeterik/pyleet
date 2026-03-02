from typing import List, Set

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for num in nums:
            num_set.add(num)
        if len(num_set) != len(nums):
            return True
        return False
    



def main():
    sol = Solution()




if __name__ == "__main__":
    main()