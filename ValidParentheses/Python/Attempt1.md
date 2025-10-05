## Time and Space Complexity

- **Time Complexity:**  
    The algorithm iterates through the string `s` exactly once, performing constant-time operations (push, pop, peek) for each character. Thus, the time complexity is **O(n)**, where *n* is the length of the input string.

- **Space Complexity:**  
    In the worst case (all opening brackets), the stack will store all characters, so the space complexity is **O(n)**.

```Python
class Solution:
    def isValid(self, s: str) -> bool:
        a = list(s)
        stack = Stack()
        
        # Mapping of closing → opening
        pairs = {")": "(", "}": "{", "]": "["}
        
        for i in a:
            if i in ["(", "{", "["]:
                stack.push(i)
            elif i in [")", "}", "]"]:
                b = stack.peek()
                if not b:   # stack is empty
                    return False
                if b == pairs[i]:  # correct match
                    stack.pop()
                else:
                    return False  # mismatch
        
        # At the end, stack must be empty
        return stack.isEmpty()
        

class Stack:
    def __init__(self):
        super()
        self.__ult_ls = list()
    def push(self, a):
        """
        Add item to Stack.
        """
        self.__ult_ls.append(a)
    def pop(self):
        """
        Remove and return last item from Stack.
        """
        b = self.__ult_ls.pop()
        return b
    def peek(self):
        if self.__ult_ls:
            return self.__ult_ls[-1]
        else:
            return False
    def isEmpty(self) -> bool:
        """
        Is Stack Empty
        """
        return not self.__ult_ls
```