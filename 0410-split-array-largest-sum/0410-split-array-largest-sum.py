class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        low = max(nums)
        high = sum(nums)

        while low <= high:
            mid = (low + high )//2

            if self.cansub(nums , mid , k):
                high = mid - 1
            else:
                low = mid +1
        return low
    
    def cansub(self , nums ,mid ,k):
        cnt = 1
        curr_sub = 0
        for i in nums:
            if curr_sub + i > mid:
                cnt +=1
                curr_sub = i
            else:
                curr_sub += i
        return cnt <= k
        