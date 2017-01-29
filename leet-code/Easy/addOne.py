class Solution(object):
    def plusOne(self, digits):
        return plus_one(digits)

def plus_one(digits):
    extra = 1
    ret = []
    
    for digit in reversed(digits):
        sum = digit + extra
        if sum > 9:
            extra = sum / 10
        else:
            extra = 0

        ret.append(sum % 10)

    if extra > 0:
        ret.append(extra)

    return list(reversed(ret))

assert plus_one([1, 2, 3]) == [1, 2, 4]
assert plus_one([0]) == [1]
assert plus_one([9]) == [1, 0]