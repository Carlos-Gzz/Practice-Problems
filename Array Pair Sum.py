# My Array Pair Sum Solution
# Given several numbers (at least 2) find the combinations that gives you the sum k.
def pair_sum(arr, k):
    if len(arr) < 2:
        return ("Not enought elements ")
    # Sets for tracking the elements.
    seen = set()
    output = set()
    # The first thing we are doing is having the difference between the sum (k) needed, and the num (element).
    for num in arr:
        target = k - num
        # With the above, we can now look for that difference in the array, if found it means we have a pair sum solution.
        if target not in seen:
            seen.add(num)

        else:
            output.add(((min(num, target)), max(num, target)))

    return output

