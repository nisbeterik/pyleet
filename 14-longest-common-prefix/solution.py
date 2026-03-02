from typing import List

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        longest = ""
        
        if len(strs) == 1:
            return strs[0]
        
        for c in range(len(strs[0])):
            for j in range(1, len(strs)):
                if c >= len(strs[j]) or strs[0][c] != strs[j][c]:
                    return longest
            longest += strs[0][c]
        
        return longest  
    

def main():
    sol = Solution()
    strs = ["cir", "car"]
    longest = sol.longestCommonPrefix(strs)
    print(longest)  
    
if __name__ == "__main__":
   main()
