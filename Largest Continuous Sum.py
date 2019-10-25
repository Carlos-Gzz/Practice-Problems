#Here we are asked for the largest Continuous Sum
#Example: The largest continuous sum of this array is 29: [1,2,-1,3,4,10,10,-10,-1].
def large_cont_sum(arr):
#I decided to open a check in order to get the elements i was about to compare and keep the sum going.
    check = 0
    output = arr[0]
    for i in arr:
#In other words, if the result of arr[x] is less than check, then we shall keep adding elements to the check.
        check += i
        if output < check:
            output = check
    return output


# This was my first-fast thought solution; But it is not as efficient as the solution above (O)nation wise.
def large_cont_sum2(arr):
    if len(arr) == 0:
        return 0

    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)

    return max_sum