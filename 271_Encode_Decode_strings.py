from typing import List

class Solution:
    """
    what we did is a way to delimeter the 
    strings in the list of stringso

    based off hints we can have a number that tells us how many letters to read for the string
    the start will start with a # and we count how many before we add to the list
    """

    def first_attempt_encode(self, strs: List[str]) -> str:
        ret = ""
        for i in range(0, len(strs)):
            newWord = "#" + str(len(strs[i])) + strs[i]
            ret = ret + newWord
        return ret

    # when we encounter a # we will read the number that is next and upload that entire word next
    def first_attempt_decode(self, s: str) -> List[str]:
        ret = []
        count = 0
        while (count < len(s)):
            newWord = ""
            if s[count] == "#":
                count += 1
                wordLength = int(s[count])
                count += 1
                for i in range(0, wordLength):
                    newWord = newWord + s[count+i]
                ret.append(newWord)
            count += 1

        return ret
    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        sizes, res = [], ""
        for word in strs:
            sizes.append(len(word))

        for lengths in sizes:
            res += str(lengths) + ","

        res += "#"
        for w in strs:
            res += w

        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes = []
        i = 0
        res = []

        number = ""
        while s[i] != "#":
            if s[i] == ",":
                sizes.append(int(number))
            number += s[i]
            i+=1 
        i+=1

        for size in sizes:
            newWord = s[i:i + size]
            i += size

        return res


"""
encode the sizes upfront in the beginning 
then we will process the strings in the regular list
the reason is beause there might be special characters so we can really us a delimter because 
that can be included in the word

"""









