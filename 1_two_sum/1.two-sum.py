#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index in range(len(nums)):
            for anotherIndex in range(len(nums)):
                if index == anotherIndex:
                    continue
                elif nums[index] + nums[anotherIndex] == target:
                    return [index, anotherIndex]
# @lc code=end

