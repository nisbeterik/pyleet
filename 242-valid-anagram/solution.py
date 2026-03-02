class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for l in s:
            if l not in d:
                d[l] = 1
                continue
            value = d[l]
            value = value+1
            d.update({l: value})
        d2 = {}
        for l in t:
            if l not in d2:
                d2[l] = 1
                continue
            value = d2[l]
            value = value+1
            d2.update({l: value})
        if d == d2:
            return True
        else:
            return False