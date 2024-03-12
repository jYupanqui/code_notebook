"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints
of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.



Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water
 (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1


Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""
from typing import List


# O(N) linear solution

def max_area(height: List[int]) -> int:
    """
    O(n)
    :param height:
    :return:
    """
    area: int = 0
    l, r = 0, len(height) - 1

    while l < r:
        temp_area = min(height[l], height[r]) * (r - l)
        area = max(area, temp_area)

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return area


x = [1, 8, 6, 2, 5, 4, 8, 3, 7]

assert max_area(x) == 49, f"Area Failed it should be 49"

