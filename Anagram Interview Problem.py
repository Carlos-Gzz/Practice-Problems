# We are given n and m strings and are asked to check if given strings are an anagram
# This anagram algorithm could be used for auto-correct forms tests
def anagram2(n, m):
    n = n.replace(" ", "").lower()
    m = m.replace(" ", "").lower()

    # Edge case check
    if len(n) != len(m):
        return False
    # Lets open a count for the finite number of letters given in the word.
    count = {}
    # If the letter in n is already in count, count shall be its value+1, otherwise it shall be 1.
    for letter in n:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    # The same goes for m. But this time, we are substracting 1, so the numbers could get to an even match.
    for letter in m:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1
    # Here we check if k is 0, if it is; it means that the letters in n are the same letters in m.
    for k in count:
        if count[k] != 0:
            return False
    return True