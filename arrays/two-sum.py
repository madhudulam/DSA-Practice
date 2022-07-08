#Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.
from typing import List
class Solution:
    def twoSum(self, nums:List[int], target:int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i

        for i in range(len(nums)):
            complement = target - nums[i]            
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]

ob = Solution()
print(ob.twoSum(nums = [2,7,11,15], target = 9))
# print(ob.twoSum(nums = [3,2,4], target = 6))
# print(ob.twoSum(nums = [3,3], target = 6))

# Time complexity: O(n)O(n). We traverse the list containing nn elements exactly twice. Since the hash table reduces the lookup time to O(1)O(1), the overall time complexity is O(n)O(n).
# Space complexity: O(n)O(n). The extra space required depends on the number of items stored in the hash table, which stores exactly nn elements.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]