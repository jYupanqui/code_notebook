"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters
include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.



Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.


Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""
import re


def is_palindrome2(s: str) -> bool:
    new_str = ""
    for c in s:
        if c.isalnum():
            new_str += c.lower()
    return new_str == new_str[::-1]


def is_palindrome3(s: str) -> bool:
    """
    Using two pointers. No extra memory needed.
    :param s:
    :return:
    """

    l, r = 0, len(s) - 1

    while l < r:
        while l < r and not alpha_num(s[l]):
            l += 1
        while r < l and not alpha_num(s[l]):
            l -= 1

        if s[l].lower() != s[r].lower():
            return False

        l, r = l + 1, r - 1
    return True


def alpha_num(c):
    """
    with ord function we get the ASCII value of the character
    :param c:
    :return:
    """
    return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9')
            )


def is_palindrome(s: str) -> bool:
    cs: str = re.sub("[^0-9a-zA-Z\s]+", "", s).replace(" ", "").lower()
    csr: str = cs[::-1]
    print(cs, csr)
    return True if cs == csr else False


print(is_palindrome("tacocat"))

print(is_palindrome("A man, a plan, a canal: Panama"))
