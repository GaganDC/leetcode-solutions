class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1


        left , right  = 0,len(nums1) 
        n = len(nums1) 
        m = len(nums2)

        while left <= right:

            i = (left + right)//2
            j = (n + m +1)//2-i

            num1_left_max = float('-inf') if i == 0 else nums1[i-1]
            num1_right_min = float('inf')  if i == n else nums1[i]
            num2_left_max = float('-inf')  if j == 0 else  nums2[j-1]
            num2_right_min = float('inf')  if j == m else nums2[j]


            if num1_left_max <=  num2_right_min and num2_left_max <= num1_right_min:

                if (n+m)%2 == 0:
                    return (max(num1_left_max ,num2_left_max) + min(num1_right_min ,num2_right_min))/2.0

                else:
                    return max(num1_left_max ,num2_left_max)
            elif num1_left_max > num2_right_min:
                right = i -1
            else:
                left = i +1
        