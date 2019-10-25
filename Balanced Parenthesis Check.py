# My solution to the Balanced Parenthesis Check
# Check if parenthesis opens matches with closes.
# Example. "([])" True, "([)]" False
def balance_check(s):
    if len(s) % 2 != 0:
        return False
    # Here i stated that these are the only elements it should be opening, otherwise it wont match with a close.
    opening = set("([{")
    # Here i stated the matching elements.
    matches = set([("(", ")"), ("{", "}"), ("[", "]")])
    # Lets open our stack of elements
    stack = []
    # Algo time! Here we are appending the elements in the stack in order to check for future matches.
    for paren in s:

        if paren in opening:
            stack.append(paren)
        else:
            if len(stack) == 0:
                return False
            # Here we state the stack.pop() in order to check for the matching element in the other side.
            last_open = stack.pop()
            # If they are in match, the algo shall continue to the next element check, otherwise it shall return False.
            if (last_open, paren) not in matches:
                return False

    return len(stack) == 0
