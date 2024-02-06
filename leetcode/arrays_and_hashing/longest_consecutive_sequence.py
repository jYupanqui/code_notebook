"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.



Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore, its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9


Constraints:

0 <= nums.Length <= 105
-109 <= nums[i] <= 109
"""
from typing import List


def longest_consecutive(nums: List[int]) -> int:
    num_set: set = set(nums)
    longest_seq: int = 0

    for n in nums:
        # Check if it's a sequence start
        if (n - 1) not in num_set:
            seq_len: int = 0
            while (n + seq_len) in num_set:
                seq_len += 1

            longest_seq = max(seq_len, longest_seq)

    return longest_seq


# Tests
numss = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]

print(longest_consecutive(nums=numss))
