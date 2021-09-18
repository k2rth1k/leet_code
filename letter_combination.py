"""
    ref:https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""


from typing import List


class Solution:
    digit_map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    combos = []

    def letterCombinations(self, digits: str) -> List[str]:
        for alphabet in self.digit_map[digits[0]]:
            combo = ''
            self.letter_combo(digits[1:], combo + alphabet)
        return self.combos

    def letter_combo(self, digits, combo):
        if digits == '':
            self.combos.append(combo)
            return
        for alphabet in self.digit_map[digits[0]]:
            self.letter_combo(digits[1:], combo + alphabet)


if __name__ == "__main__":
    print(Solution().letterCombinations('2345'))
