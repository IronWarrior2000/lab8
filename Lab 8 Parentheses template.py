class Stack:
    def __init__(self):
        # Initialize an empty list to store stack items
        self.items = []

    def is_empty(self):
        # Return True if the stack is empty, otherwise False
        return len(self.items) == 0
        
        
    def push(self, item):
        # Add an item to the top of the stack
        self.items.append(item)

    def pop(self):
        # Remove and return the top item from the stack if it's not empty
        # If the stack is empty, return None
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        # Return the top item without removing it if the stack is not empty
        # If the stack is empty, return None
        if not self.is_empty():
            return self.items[-1]
        else: 
            return None

def is_balanced(expression):
    # Create a stack to keep track of opening parentheses
    stack = Stack()

    # Define matching pairs for parentheses
    opening = "({["
    closing = ")}]"
    matches = {')': '(', '}': '{', ']': '['}

    # Loop through each character in the expression
    for char in expression:
        # Check if the character is an opening parenthesis
        if char in opening:
            # Push the opening parenthesis to the stack
            stack.push(char)

        # Check if the character is a closing parenthesis
        elif char in closing:
            # If stack is empty or top of stack doesn't match the closing parenthesis, return False
            # Otherwise, pop the top of the stack
            if stack.is_empty() or stack.peek() != matches[char]:
                return False
            stack.pop()

    # If stack is empty, all parentheses were matched; otherwise, return False
    return stack.is_empty() 

# Test cases 
expression1 = "({X+Y}*Z)"
expression2 = "{X+Y}*Z)"
expression3 = "({X+Y}*Z"
expression4 = "[A+B]*({X+Y}]*Z)"

# Expected output: True, False, False, False respectively
print(is_balanced(expression1))
print(is_balanced(expression2))
print(is_balanced(expression3))
print(is_balanced(expression4))
