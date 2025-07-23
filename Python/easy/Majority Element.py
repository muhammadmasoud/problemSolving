def majorityElement(nums):
        dic = {}
        for i in nums:
            if i in dic.keys():
                dic[i] += 1
            else:
                dic[i] = 1
        maxx = max(dic, key=dic.get)
        return maxx

'''def majorityElement(nums):
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate'''