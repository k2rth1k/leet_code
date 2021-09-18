"""
    ref: https://leetcode.com/problems/trapping-rain-water/
"""
from typing import List

"""
    
    logic: 
    step :1) find out tallest towers on both right and left side to the tower in current index.
    step :2) rain water = {
                            for i range(length):
                                minimum = min(tallest_right_tower, tallest_left_tower)
                                if i < minimum:
                                    rain_water = rain_water + minimum - height


"""


class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        right_tallest_tower = [0] * length
        maximum_height = 0
        i = length - 1
        while i >= 0:
            if height[i] >= maximum_height:
                maximum_height = height[i]
            right_tallest_tower[i] = maximum_height
            i = i - 1
        rain_water = 0

        max_left_height = 0
        for i in range(length):
            if max_left_height <= height[i]:
                max_left_height = height[i]
            minimum = min(right_tallest_tower[i], max_left_height)
            if height[i] < minimum:
                rain_water = rain_water + minimum - height[i]

        return rain_water


def main():
    sol = Solution()
    print(sol.trap([0, 1, 0, 3, 4, 6, 1, 6, 6, 7, 2, 1, 2, 1]))


if __name__ == "__main__":
    main()
