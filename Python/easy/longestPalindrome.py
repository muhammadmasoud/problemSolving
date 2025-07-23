def longestPalindrome(s):
            freq_arr = [0] * 128
            for c in s:
                freq_arr[ord(c)] += 1

            ans = 0
            for count in freq_arr:
                ans += count // 2 * 2 
            if ans < len(s):  
                ans += 1
            return ans