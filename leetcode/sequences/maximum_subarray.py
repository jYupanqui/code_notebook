"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104


Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

Using Kadane's algorithm
https://www.interviewbit.com/blog/maximum-subarray-sum/#:~:text=Kadane's%20Algorithm%20is%20an%20iterative,ending%20at%20the%20previous%20position.

Solution:
https://leetcode.com/problems/maximum-subarray/discuss/1595195/C%2B%2BPython-7-Simple-Solutions-w-Explanation-or-Brute-Force-%2B-DP-%2B-Kadane-%2B-Divide-and-Conquer


"""
from math import inf


def max_sub_array(nums: list[int]) -> int:
    ans = -inf
    for i in range(len(nums)):
        cur_sum = 0
        for j in range(i, len(nums)):
            cur_sum += nums[j]
            ans = max(ans, cur_sum)
    return ans


r = max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4])

print(r)
