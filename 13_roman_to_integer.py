# https://leetcode.com/problems/roman-to-integer/description/

class Solution():
    def romanToInt(self, s):
        roman_ref_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,

            'IV': 4,
            'IX': 9,

            'XL': 40,
            'XC': 90,

            'CD': 400,
            'CM': 900
        }

        split_letters = []
        iterator_a = 0
        result = 0

        while iterator_a < len(s):
            
            if s[iterator_a] == 'I' and (iterator_a + 1) < len(s):
                if s[iterator_a + 1] == 'V' or s[iterator_a + 1] == 'X':
                    split_letters.append(s[iterator_a] + s[iterator_a + 1])
                    iterator_a += 1
                else:
                    split_letters.append(s[iterator_a])
            elif s[iterator_a] == 'X' and (iterator_a + 1) < len(s):
                if s[iterator_a + 1] == 'L' or s[iterator_a + 1] == 'C':
                    split_letters.append(s[iterator_a] + s[iterator_a + 1])
                    iterator_a += 1
                else:
                    split_letters.append(s[iterator_a])
            elif s[iterator_a] == 'C' and (iterator_a + 1) < len(s):
                if s[iterator_a + 1] == 'D' or s[iterator_a + 1] == 'M':
                    split_letters.append(s[iterator_a] + s[iterator_a + 1])
                    iterator_a += 1
                else:
                    split_letters.append(s[iterator_a])
            else:
                split_letters.append(s[iterator_a])
            iterator_a += 1

        for i in range(0, len(split_letters)):
            result = result + roman_ref_dict[split_letters[i]]

        print(result)
        return result
            

sol = Solution()
sol.romanToInt('MDLXX')