class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        if (nums1.length == 0) {
            System.out.println(1 + "null");
            if (nums2.length % 2 == 0) {
                return (Double.valueOf(nums2[nums2.length / 2 - 1]) + Double.valueOf(nums2[nums2.length / 2])) / 2;
            }
            else {
                return Double.valueOf(nums2[nums2.length / 2]);
            }
        }
        else if (nums2.length == 0) {
            System.out.println(2 + "null");
            if (nums1.length % 2 == 0) {
                return (Double.valueOf(nums1[nums1.length / 2 - 1]) + Double.valueOf(nums1[nums1.length / 2])) / 2;
            }
            else {
                return Double.valueOf(nums1[nums1.length / 2]);
            }
        }
        else {
            if (nums1.length < nums2.length) {
                return binsearch(nums1, nums2);
            }
            else {
                return binsearch(nums2, nums1);
            } 
        }
    
    }

    public static double binsearch(int[] a, int[] b) {
        int half = (a.length + b.length) / 2;

        int left = 0;
        int right = a.length - 1;
        while (left <= right) {
            int i = left + (right - left) / 2;
            int j = half - i;
            int maxLeft1;
            int minRight1;
            int maxLeft2;
            int minRight2;
            // maxLeft1 < minRight2 && maxLeft2 < minRight1
            if (i == 0) {
                maxLeft1 = Integer.MIN_VALUE;
                
            }
            else {
                maxLeft1 = a[i - 1];
                
            }
            if (j == 0) {
                maxLeft2 = Integer.MIN_VALUE;
                
            }
            else {
                maxLeft2 = b[j - 1];
            
            }
            if (j >= b.length) {
                minRight2 = Integer.MAX_VALUE;
            }
            else {
                minRight2 = b[j];
            }
            if (i >= a.length) {
                minRight1 = Integer.MAX_VALUE;
            }
            else {
                minRight1 = a[i];
            }

            if (maxLeft1 <= minRight2 && maxLeft2 <= minRight1) {
                if (a.length % 2 == 0) {
                    double l = Math.max(maxLeft1, maxLeft2);
                    double r = Math.min(minRight1, minRight2);
                    return (l + r) / 2;
                }
                else {
                    double result = Math.min(minRight1, minRight2);
                    return result;
                }
            }
            else if (maxLeft1 > minRight2) {
                right = i - 1;
            }
            else if (maxLeft2 > minRight1) {
                left = i + 1;
            }
        }
        return 0;
    }
}
