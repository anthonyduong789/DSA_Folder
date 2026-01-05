class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool

        for this anagram we will also have to make sure that the 
        frequency of characters are also the same
        """
        
        countFrequencyS = {}
        for item in s:
            if item in countFrequencyS: 
                countFrequencyS[item] = countFrequencyS[item] + 1
            else:
                countFrequencyS[item] = 1

        for item2 in t: 
            if item2 in countFrequencyS:
                countFrequencyS[item] = countFrequencyS[item] - 1
                if countFrequencyS[item] == 0:
                    countFrequencyS.pop(item)
            else: 
                return False

        if len(countFrequencyS) != 0:
            return False
            
        return True
                

            

        

        
