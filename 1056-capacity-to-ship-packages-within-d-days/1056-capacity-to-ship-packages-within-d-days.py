class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        n = len(weights)

        low = max(weights)

        high = sum(weights)

        while low <= high:
            mid =(low + high )//2

            if self.canship(weights,mid,days):
                high = mid -1
            else:
                low = mid +1
        return low 


    def canship(self,weights,mid, days):
        n = len(weights)

        curr_w = 0
        days_c = 1

        for w in weights:
            if curr_w + w > mid:
                days_c +=1
                curr_w = w
            else:
                curr_w += w

        return days_c <= days

    

        