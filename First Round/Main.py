class palindrome:
    def __init__(self,val):
        self.str = val

    def checkPalindrome(self):
        t = self.str

        res =""

        for i in t:
            res = i + res

        if self.str == res:
            print(self.str,"is palindrome")
        else:
            print(self.str,"is not palindrome")

if __name__ == '__main__':
    val = "rar"

    palin = palindrome(val)
    palin.checkPalindrome()
