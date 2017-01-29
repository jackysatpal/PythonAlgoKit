class Solution(object):
    def lengthOfLastWord(self, s):
        last_word = get_last_word(s)
        if not last_word:
            return 0

        return len(last_word) # This is trivially simple to implement

def get_last_word(string):
    if not string:
        return None

    words = get_words(string)

    if not words:
        return None

    return words[len(words) - 1]

def get_words(string):
    if not string:
        return []

    buffer = ''
    words = []
    for char in string:
        if char == ' ' and buffer: # Valid word detected
            words.append(buffer)
            buffer = ''
            continue
        elif char == ' ' and not buffer: # Not a valid word
            continue

        buffer += char

    if buffer:
        words.append(buffer)

    return words

assert get_words('Hello world') == ['Hello', 'world']
assert get_words('one') == ['one']
assert get_words('') == []
assert get_words(None) == []
assert get_words(' ') == []
assert get_words('  ') == []
assert get_words('  Hello world') == ['Hello', 'world']