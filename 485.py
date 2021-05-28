class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        currentCount = 0    
        highestConsecCount = 0
    
        for number in nums:
            if number == 1:
                currentCount += 1
                highestConsecCount = max(currentCount,highestConsecCount)
                    
            else:
                currentCount = 0
        
        return highestConsecCount
