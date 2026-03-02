class Solution:
    def romanToInt(self, s: str) -> int:
        rom_dick = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        total = 0
        for i in range(len(s)):
            total+=rom_dick[s[i]]
        return total
        

def main():
    sol = Solution()
    result = sol.romanToInt("LVIII")
    print(result)
                            

if __name__ == "__main__":
    main()
        