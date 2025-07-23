def findMissingnum(ls):
    n = len(ls) + 1
    expected_sum = n*(n+1)//2
    actual_sum = sum(ls)
    return expected_sum - actual_sum