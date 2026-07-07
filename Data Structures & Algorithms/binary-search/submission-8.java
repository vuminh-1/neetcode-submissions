class Solution {
    public int search(int[] nums, int target) {
        if (target < nums[0]){
            return -1;
        }
        else if (target > nums[nums.length - 1]){
            return -1;
        }
        
        int l = 0;
        int r = nums.length - 1;
        if (nums[l] == target){
            return l;
        }
        else if (nums[r] == target){
            return r;
        }
        while (l != r){
            if (nums[l] == target){
                return l;
            }
            else if (nums[r] == target){
                return r;
            }
            else{
                int mid = (l + r) / 2;
                if (nums[mid] == target){
                    return mid;
                }
                else if (nums[mid] > target){
                    r = mid - 1;
                }
                else if (nums[mid] < target){
                    l = mid + 1;
                }
            }
        }
        return -1;
    }
}
