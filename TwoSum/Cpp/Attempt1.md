# Intuition
To solve the problem I thought I would burrow techniques from other Programming Languages that I have used. So I then decided that I would just try to find the complement of the target minus the value that I would be looping over.

# Approach
Using a for loop I would loop over the vector then I would search for it's complement using another method called findIndex, and if I didn't find it I would jump to the next number until I either found the solution, or if there was no solution report no solution.

# Complexity
- Time complexity:
The time complexity is $$O(n^2)$$ because of the usage of two for loops (i.e. one of them being a linear search).

- Space complexity:
The space complexity of the problem is $$O(1)$$ for this particular problem.

# Code
```cpp []
class Solution {
public:
    int findIndex(vector<int>& nums, int elem){
        for(int i=0; i<nums.size(); i++){
            if(nums.at(i) == elem){
                return i;
            }
        }
        return -1;
    };

    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> g;
        for(int i=0; i<nums.size(); ++i){
            int q = target - nums.at(i);
            nums.at(i) = INT_MIN;
            int w = findIndex(nums,q);
            if( w == -1){
                continue;
            }
            else{
                g.push_back(i);
                g.push_back(w);
                return g;
            } 
    }
    return {-1,-1};  
};
};
```