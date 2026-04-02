class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm = {}
        for letter in s:
            if letter in hm:
                hm[letter] += 1
            else:
                hm[letter] = 1
        for letter in t:
            if letter in hm:
                hm[letter] -= 1
            else:
                return False
        for letter in hm:
            if hm[letter] != 0:
                return False
        return True