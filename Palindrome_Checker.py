def Palindrome_Checker(str):
    str=str
    print(f"before performing Palindrome operation:{str}")
    rev_str=str[::-1]
    print(f"after performing Palindrome operation:{rev_str}")
    if str==rev_str:
        print("your given string is Palindrome")
    else:
        print("Not Palindrome string")
Palindrome_Checker("madam")
Palindrome_Checker("racecar")
