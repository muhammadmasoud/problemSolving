def isPalindrome(x):
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
            
    reversed_num = 0
    original = x
            
    while x > reversed_num:
        reversed_num = reversed_num * 10 + x % 10
        x = x // 10
            
    return x == reversed_num or x == reversed_num // 10


'''def isPalindrome(x):
    y = x
    ans = 0
    if y // 10 == 0:
        return True
        
    if y < 0:
        return False

    while y // 10 != 0:
        curr = y % 10
        ans += curr
        ans *= 10
        y //= 10
    curr = y % 10
    ans += curr
    return ans == x'''
