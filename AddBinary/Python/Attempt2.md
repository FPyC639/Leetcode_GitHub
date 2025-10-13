Adds two binary strings and returns their sum as a binary string.

Time Complexity: $O(\max(N, M))$, where N and M are the lengths of input strings a and b. This is due to the conversion of binary strings to integers and back.
Space Complexity: $O(\max(N, M))$, as the space required for the integer representation and the resulting binary string is proportional to the length of the inputs.

```Python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2) + int(b,2)).replace('0b','')
```