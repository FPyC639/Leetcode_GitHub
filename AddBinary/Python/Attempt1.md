Adds two binary strings and returns their sum as a binary string.
Time Complexity: $O(\max(N, M))$, where N and M are the lengths of input strings a and b.
Space Complexity: $O(\max(N, M))$, due to integer conversion and the resulting binary string.

```Python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2) + int(b,2))[2:]
```