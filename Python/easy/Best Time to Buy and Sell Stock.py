def maxProfit(l):
    buy = l[0]
    p = 0
    for i in range(1, len(l)):
        if l[i]< buy:
            buy = l[i]
        if l[i] > buy:
            if l[i] - buy > p:
                p = l[i] - buy
    return p


print(maxProfit([2,1,2,1,0,1,2]))


