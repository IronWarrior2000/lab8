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
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
        # If the stack is empty, return None
       

    def peek(self):
        # Return the top item without removing it if the stack is not empty
        # If the stack is empty, return None
        if not self.is_empty():
            return self.items[-1]
        else: 
            return None
        

def evaluate_expression(expression):
    # Initialize two stacks: one for numbers and one for operators
    num_stack = Stack()  # Stack for numbers
    op_stack = Stack()   # Stack for operators

    # Define a helper function to apply an operator to the top two numbers on num_stack
    def apply_operator():
        # Pop the top operator from op_stack
        operator = op_stack.pop()
        # Pop the top two numbers from num_stack
        num2 = num_stack.pop()
        num1 = num_stack.pop()
        # Perform the operation and push the result back to num_stack
        if operator == "+":
            num_stack.push(num1 + num2)
        elif operator == "-":
            num_stack.push(num1 - num2)
        elif operator == "*":
            num_stack.push(num1 * num2)
        elif operator == "/":
            num_stack.push(num1 / num2)
        
    
    # Define operator precedence
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    
    # Loop through each character in the expression
    i = 0
    while i < len(expression):
        char = expression[i]

        # Ignore whitespace characters
        if char == ' ':
            i += 1
            continue

        # Check if the character is a digit
        if char.isdigit():
            # Parse the entire number and push it to num_stack
            num = 0
            while i < len(expression) and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            num_stack.push(num)
            continue

        # Check if the character is an opening parenthesis '('
        elif char == '(':
            # Push '(' to op_stack to mark the start of a group
            op_stack.push(char)            

        # Check if the character is a closing parenthesis ')'
        elif char == ')':
            # Pop and apply operators until '(' is found
            while not op_stack.is_empty() and op_stack.peek() != '(':
                apply_operator()
            op_stack.pop() 

        # If it's an operator (+, -, *, /)
        elif char in "+-*/":
            # Apply operators based on precedence, then push current operator to op_stack
            while (not op_stack.is_empty() and op_stack.peek() != '(' and
                   precedence[op_stack.peek()] >= precedence[char]):
                apply_operator()
            op_stack.push(char)         
            
        # Move to the next character
        i += 1

    # After the loop, apply any remaining operators in op_stack
    while not op_stack.is_empty():
        apply_operator()

    # Return the final result from num_stack
    return num_stack.pop()

# Test cases 
expression1 = "(((6+9)/3)*(6-4))"
expression2 = "10 + (2 * (6 + 4))"
expression3 = "100 * (2 + 12) / 4"

# Expected output: 10, 30, 350 respectively
print(evaluate_expression(expression1))
print(evaluate_expression(expression2))
print(evaluate_expression(expression3))
