class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = "%s"%x #convert to string
        reverse = num[::-1] # create reverse string
        if num == reverse: #check if identical
            return True
        else:
            return False
        pass



def main():
    sol = Solution()

    num = 1221
    result = sol.isPalindrome(num)
    print(result)


if __name__ == "__main__":
    main()