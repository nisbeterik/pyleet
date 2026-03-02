from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        pass

def main():
    sol = Solution()

    
    nums = [2, 7, 11, 15]
    target = 9

    result = sol.twoSum(nums, target)

    print("Input:", nums)
    print("Target:", target)
    print("Output:", result)


if __name__ == "__main__":
    main()