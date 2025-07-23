def isPalindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

'''def isPalindrome(s):
    s2=""
    for char in range(len(s)-1, -1, -1):
        s2 += s[char]
    if s == s2:
        return True
    else:
        return False'''