##
# LeetCode question: https://leetcode.com/problems/implement-strstr
##
class Solution(object):

    def strStr(self, haystack, needle):
        return str_in_str(haystack, needle)

def str_in_str(haystack, needle):

    ret = handle_basic(haystack, needle)
    if ret != None:
        return ret

    length = len(haystack)
    for i in range(length):
        if haystack[i] == needle[0]:
            if substr_is_impossible(needle, haystack, i):
                return -1

            if check_needle_from(needle, haystack, i) != -1:
                return i
    return -1

def substr_is_impossible(needle, haystack, i):
    if len(needle) + i > len(haystack):
        return True

def check_needle_from(needle, haystack, i):
    inner_i = i
    for char in needle:
        if char != haystack[inner_i]:
            return -1
        inner_i += 1
    return i

def handle_basic(haystack, needle):

    if needle == '':
        return 0

    if not haystack:
        return -1

    if len(needle) > len(haystack):
        return -1


# Test Cases

assert str_in_str('', 'hello') == -1
assert str_in_str('', '') == 0
assert str_in_str('hello', '') == 0
assert str_in_str('x', 'hello') == -1

assert substr_is_impossible('xyz', 'mix', 2)
assert not substr_is_impossible('x', 'mix', 2)
assert not substr_is_impossible('x', 'mixpp', 2)

assert check_needle_from('hello', 'world, hello', 7)
assert check_needle_from('hello', 'world, hello   ', 7)
assert check_needle_from('hello', 'world, hello   ', 8) == -1

assert str_in_str('hello', 'x') == -1
assert str_in_str('world x hello', 'world x') == 0
assert str_in_str('hello x world', 'x') == 6
assert str_in_str('world hello x', 'world x') == -1
