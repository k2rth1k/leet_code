"""
    ref:https://leetcode.com/problems/container-with-most-water/
"""
import copy
from array import array
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        length = len(height)
        max_area = 0
        for i in range(length):
            j = i + 1
            while j < length:
                optimal_height = min(height[i], height[j])
                water = area = optimal_height * (j - i)
                if max_area < water:
                    max_area = water
                j+=1
        return max_area


if __name__ == '__main__':
    print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    pass
