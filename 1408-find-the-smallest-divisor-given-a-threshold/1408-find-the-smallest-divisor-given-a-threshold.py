class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        
        low = 1
        high = max(nums)
        

        while low <= high:
            val =0
            mid = (low + high)//2

            for num in nums:
                val += (num +mid -1)//mid

            if val <= threshold:
                high = mid -1
            else:
                low = mid +1
        return low 
            

