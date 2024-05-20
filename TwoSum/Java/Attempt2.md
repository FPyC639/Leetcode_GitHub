# Intuition
The intutition behind the problem is to develop a better algorithm and to use DataStructures to improve the output of the code and in this case the code used a Hash map but it did not result in a performance improvement.

# Approach
The approach is to use a dictionary style method where items can be accessed using keys, and values. However, it is still far an improvement from Attempt1.

# Complexity
- Time complexity:
The time complexity here still remains at $$O(n^2)$$
because I am iterating twice over the same particular object

- Space complexity:
The space complexity here according to ChatGPT is $$O(n)$$
due to the usage of hashmap.

# Code
```Java
import java.util.*;
class Solution {
    public int[] twoSum(int[] nums, int target) {
            HashMap<Integer, Integer> a = createHashTable(nums);
            return indexarr(a, target);
            
        }
    public static HashMap<Integer, Integer> createHashTable(int[] array) {
        HashMap<Integer, Integer> hashTable = new HashMap<>();
        for (int i = 0; i < array.length; i++) {
            hashTable.put(i, array[i]);
        }
        return hashTable;
    }

    public static int[] indexarr(HashMap<Integer,Integer> map,int target){
        boolean skip = true;
        int skipCount = 1; // Variable to control the number of skips

        while (true) {
            Iterator<Map.Entry<Integer, Integer>> iterator = map.entrySet().iterator();
            Integer key = null;
            Integer value = null;
            Integer key1 = null;
            Integer value1 = null;
            
            if (skip) {
                for (int i = 0; i < skipCount; i++) {
                    if (iterator.hasNext()) {
                        Map.Entry<Integer, Integer> entry = iterator.next();
                        value = entry.getValue();
                        key = entry.getKey();
                    } else {
                        return null; // Exit if we run out of entries
                    }
                }
                skip = false; // Set skip to false after skipping
            }

            while (iterator.hasNext()) {
                Map.Entry<Integer, Integer> entry = iterator.next();
                value1 = entry.getValue();
                key1 = entry.getKey();
                if (value + value1 == target) {
                    System.out.println("Target " + target + " found with keys " + key + " and " + key1);
                    return new int[]{key, key1};
                }
            }

            // Reset skip to true and increment skipCount for the next outer iteration
            skip = true;
            skipCount++;
            if (skipCount > map.size()) {
                return null; // Exit if skipCount exceeds the number of entries
            }
        }
    }
        //if (iterator.hasNext()) {
        //    iterator.next();
        //}
        //Integer key1 = 0;
        //Integer temp = map.get(key1);
        //while (iterator.hasNext()) {
        //    Map.Entry<Integer, Integer> entry = iterator.next();
        //    Integer key = entry.getKey();
        //    Integer value = entry.getValue();
        //    if(temp+value == target){
        //        return new int [] {key1,key};
        //    }
        //    key1 += 1;
        //    temp = map.get(key1);
    //}
     //   return null;
    }

```