# Intuition
The intutition behind this approach was that the list of key and values from the enumerate can be used in a dictionary.

# Approach
Using the dictionary method I can access keys and values and then use that to find the value that I am looking for in the particuar problem.

# Complexity
- Time complexity:
The time complexity for this problem is $$O(n^2)$$ since there is double for loop.

- Space complexity:
The space complexity here is $$O(n)$$
because a dictionary was used which is similar to a hashmap.

# Code
```Python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.a = dict(enumerate(nums))
        self.key = 0
        self.value = self.a.get(self.key,None)
        while(self.key < len(self.a) ):
            self.key1 = self.key + 1
            while(True):
                self.value1 = self.a.get(self.key1,0)
                if(self.value + self.value1 == target):
                    return [self.key,self.key1]
                if(self.key1>len(self.a)):
                    break
                self.key1 += 1 
            self.key +=1
            self.value = self.a.get(self.key,None)

```
# Code 2
```
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.a = dict(enumerate(nums))
        self.key = 0
        self.value = self.a.get(self.key,None)
        self.len_a = len(self.a)
        while(self.key < self.len_a ):
            self.key1 = self.key + 1
            while(True):
                self.value1 = self.a.get(self.key1,0)
                if(self.value + self.value1 == target):
                    return [self.key,self.key1]
                if(self.key1>self.len_a):
                    break
                self.key1 += 1 
            self.key +=1
            self.value = self.a.get(self.key,None)

```