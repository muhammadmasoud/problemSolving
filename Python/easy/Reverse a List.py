def reverse(ls):
    rev_ls = []
    for i in range(len(ls)-1,-1,-1):
        rev_ls.append(ls[i])
    return rev_ls