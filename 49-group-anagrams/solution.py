from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alpha = {"a": 2, "b": 3, "c": 5, "d": 7, "e": 11, "f": 13, "g": 17, "h": 19, "i": 23, "j": 29, "k": 31, "l": 37, "m": 41, "n": 43, "o": 47, "p": 53, "q": 59, "r": 61, "s": 67, "t": 71, "u": 73, "v": 79, "x": 83, "y": 89, "z": 97}
        d = dict()
        for str in strs:
            value = 0
            for c in str:
                value = value*alpha[c]
            d.setdefault(value, []).append(str)
        return list(d.values())