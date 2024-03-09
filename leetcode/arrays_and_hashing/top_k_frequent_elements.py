"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.


Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.



Could be done with bucket sort.
"""


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    map = {}
    feq = [[] for i in range(len(nums) + 1)]

    for n in nums:
        map[n] = 1 + map.get(n, 0)

    for n, c in map.items():
        feq[c].append(n)

    res = []
    for i in range(len(feq) - 1, 0, -1):
        for n in feq[i]:
            res.append(n)
            if len(res) == k:
                return res


test = [1, 1, 1, 2, 2, 3, 3, 3, 3, 3]
test_k = 2

top_k_frequent(test, test_k)
