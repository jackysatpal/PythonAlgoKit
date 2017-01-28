"""
    LeetCode Problem::https://leetcode.com/problems/string-to-integer-atoi/
"""

INT_MAX = 2147483647
INT_MIN = -2147483648

class Solution(object):
    def myAtoi(self, str):
        return toi(str)

def toi(str):
    if not str:
        return 0

    str = str.strip()

    length = len(str)
    if length == 0:
        return 0

    number = 0
    sign = False
    for i in range(length):
        msd = str[i]

        if msd == '-' or msd == '+':
            if sign:
                return 0

            sign = msd
            continue
        elif char_to_int(msd) == -1:
            break
        else:
            number_temp = number * 10 + char_to_int(msd)

        if sign != '-' and number_temp > INT_MAX:
            return INT_MAX

        if sign == '-' and number_temp * -1 < INT_MIN:
            return INT_MIN

        number = number_temp

    if str[0] == '-':
        number *= -1

    return number

def char_to_int(char):
    if char == '0':
        return 0
    elif char == '1':
        return 1
    elif char == '2':
        return 2
    elif char == '3':
        return 3
    elif char == '4':
        return 4
    elif char == '5':
        return 5
    elif char == '6':
        return 6
    elif char == '7':
        return 7
    elif char == '8':
        return 8
    elif char == '9':
        return 9

    return -1

assert toi("1234") == 1234
assert toi(" 1234 ") == 1234
assert toi(" +1234 ") == 1234
assert toi("-1234") == -1234
assert toi("-1") == -1
assert toi("1") == 1
assert toi("  1") == 1
assert toi("  1ab") == 1
assert toi("  1ab1") == 1
assert toi("") == 0
assert toi("    .") == 0
assert toi("+-1") == 0
assert toi(None) == 0
assert toi("2147483647") == 2147483647
assert toi("-2147483647") == -2147483647
assert toi("-9223372036854775808") == -2147483648
assert toi("9223372036854775808") == 2147483647
