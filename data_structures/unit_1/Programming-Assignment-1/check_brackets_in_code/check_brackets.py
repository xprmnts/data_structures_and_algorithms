# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
    text = sys.stdin.read()

    opening_brackets_stack = []
    for i, next in enumerate(text, start = 1):
        if next == '(' or next == '[' or next == '{':
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i))

        if next == ')' or next == ']' or next == '}':
            # Process closing bracket, write your code here
            if not opening_brackets_stack:
                print(i)
                sys.exit()
            top = opening_brackets_stack.pop()
            if not top.Match(next):
                print(i)
                sys.exit()

    # Printing answer, write your code here
    if opening_brackets_stack:
        top = opening_brackets_stack.pop()
        print(top.position)
        sys.exit()

    print("Success")
    sys.exit()
