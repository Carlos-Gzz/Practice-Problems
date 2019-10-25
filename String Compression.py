# We are asked to print out a 'compressed' version of the string given
# Example: AAAABBBCCaa, shall return as A4B3C2a2.
def compress(s):
    # I opened a count to count each letter individually, simple and coding efficient.
    count = {}

    for letter in s:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    print(str(count))