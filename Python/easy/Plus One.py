def plusOne(digits):
    for num in range(len(digits) - 1, -1, -1):
        if digits[num] == 9:
            digits[num] = 0
        else:
            digits[num] += 1
            return digits
        

    digits.insert(0,1)
    return digits