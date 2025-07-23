def isAnagram(s, t):
        return sorted(s) == sorted(t)
print(isAnagram("car", "rat"))