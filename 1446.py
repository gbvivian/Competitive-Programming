class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        prevChar = ""

        currCount = 0
        maxCount = 0

        for currChar in s:
            if currChar != prevChar:
                currCount = 1

            else:
                currCount += 1

            maxCount = max(currCount, maxCount)
            prevChar = currChar
        
        return maxCount
