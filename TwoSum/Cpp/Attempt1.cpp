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