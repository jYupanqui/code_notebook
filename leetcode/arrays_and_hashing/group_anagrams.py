"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the
original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]


Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.





--- Alternative solutions ---





"""
from collections import defaultdict


def group_anagrams(strs: list[str]) -> list[list[str]]:
    res = defaultdict(list)  # mapping charCount to list of Anagrams , time complexity 0(m * n)
    for s in strs:
        count = [0] * 26  # a ... z
        for c in s:
            count[ord(c) - ord("a")] += 1
        res[tuple(count)].append(s)
    return res.values()



# def group_anagrams(strs: list[str]) -> list[list[str]]:
#     sorted_map = {}
#
#     for item in strs:
#         sorted_item = "".join(sorted(item))
#         if sorted_item in sorted_map:
#             sorted_map[sorted_item].append(item)
#         else:
#             sorted_map[sorted_item] = [item]
#
#     return [*sorted_map.values()]


test = ["eat", "tea", "tan", "ate", "nat", "bat"]
back = group_anagrams(test)
back2 = group_anagrams(["a"])
back3 = group_anagrams([""])
print(back)
