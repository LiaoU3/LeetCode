class Solution:
    def intToRoman(self, num: int) -> str:
        count = 0
        ans = ""
        map1 = ['V', 'L', 'D'] # 5
        map2 = ['I', 'X', 'C', 'M'] # 1
        while num != 0:
            curr_digit = num % 10
            if curr_digit == 4:
                ans = map2[count] + map1[count] + ans
            elif curr_digit == 9:
                ans = map2[count] + map2[count+1] + ans
            elif curr_digit == 5:
                ans = map1[count] + ans
            else:
                if curr_digit > 5:
                    ans = map1[count] + map2[count] * (curr_digit - 5) + ans
                else:
                    ans = map2[count] * curr_digit + ans
            count += 1
            num = num//10

        return ans