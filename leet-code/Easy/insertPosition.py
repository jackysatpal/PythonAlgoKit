"""
    LeetCode::https://leetcode.com/problems/search-insert-position/
"""
class Solution(object):
    def searchInsert(self, nums, target):
        return _binary_search(nums, 0, len(nums) - 1, target - .1)

def _binary_search(lst, start, end, target):
    if not lst:
        return 0

    middle = _get_middle(start, end)

    if middle == start and target < lst[middle]:
        return middle
    if lst[middle - 1] < target < lst[middle]:
        return middle

    if middle == end and target > lst[middle]:
        return middle + 1
    if lst[middle] < target < lst[middle + 1]:
        return middle + 1

    # recur as necessary
    if target < lst[middle]:
        return _binary_search(lst, start, middle - 1, target)
    if target > lst[middle]:
        return _binary_search(lst, middle + 1, end, target)

def _get_middle(start, end):
    return int((start + end) / 2)

assert _get_middle(1, 3) == 2
assert _get_middle(1, 5) == 3
assert _get_middle(1, 4) == 2
assert _get_middle(1, 1) == 1

# Simple case without recursion
assert _binary_search([1, 2, 3], 0, 2, 1.5) == 1
# Simple case with recursion
assert _binary_search([1, 2, 3, 4, 5, 6, 7], 0, 6, 2.1) == 2

# Now some corner cases
assert _binary_search([], 0, 0, 1.1) == 0
print _binary_search([1], 0, 0, 1.1)
assert _binary_search([1], 0, 0, 1.1) == 1
assert _binary_search([1], 0, 0, 0.1) == 0