class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        highestCandyCount = max(candies)
        greatestCandyCandidates = []
        
        for i in range(0, len(candies)):
            if extraCandies + candies[i] >= highestCandyCount:
                greatestCandyCandidates.append(True)
            else:
                greatestCandyCandidates.append(False)
                
        return greatestCandyCandidates
