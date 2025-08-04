def romanToInt(self, s: str) -> int:
    mydic = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
        }

    ptr1 = 0
    ptr2 = 1
    ans = 0

    while ptr2 < len(s):
        if mydic[s[ptr2]] <= mydic[s[ptr1]]:
            ans += mydic[s[ptr1]]
            ptr1 += 1
            ptr2 += 1
        else:
            ans += mydic[s[ptr2]] - mydic[s[ptr1]]
            ptr1 += 2
            ptr2 += 2

    if ptr1 == len(s)-1:
        ans+= mydic[s[ptr1]]
    return ans