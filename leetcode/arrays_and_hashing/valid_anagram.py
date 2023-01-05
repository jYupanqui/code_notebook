"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false


Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""
"""
Alternative solutions:

----------------------------------------------
def check(s1, s2):
     
    # the sorted strings are checked
    if(sorted(s1)== sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")        
         
# driver code 
s1 ="listen"
s2 ="silent"
check(s1, s2)

Time Complexity: O(nlogn)

Auxiliary Space: O(1)

----------------------------------------------

# Python3 program for the above approach
from collections import Counter
 
# function to check if two strings are
# anagram or not
def check(s1, s2):
   
    # implementing counter function
    if(Counter(s1) == Counter(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")
 
 
# driver code
s1 = "listen"
s2 = "silent"
check(s1, s2)

Time Complexity: O(n)

Auxiliary Space: O(1)

----------------------------------------------




Neetcode solution

def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    countS, countT = {}, {}
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i],0)
        countS[t[i]] = 1 + countS.get(t[i], 0)
    for c in countS:
        if countS[c] != countT.get(c,0):
            return False
    return True

Time Complexity: O(s + t)

Auxiliary Space: O(1)


"""


def is_anagram(s: str, t: str) -> bool:
    s_list = list(s)
    t_list = list(t)

    ret = False

    if len(s_list) == len(t_list):

        for char in s_list:

            if char in t_list:
                for i, t_char in enumerate(t_list):
                    if char == t_char:
                        t_list.pop(i)
                        break
            else:
                break

        if len(t_list) == 0:
            ret = True

    return ret


print(is_anagram("anagram", "nagaram"))
print(is_anagram("rat", "car"))
print(is_anagram("ab", "a"))
