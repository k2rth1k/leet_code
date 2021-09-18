"""
    ref: https://leetcode.com/problems/maximum-subarray/submissions/
"""


class Solution:
    def Max_subarray(self, nums: [int]) -> int:
        summation = nums[0]
        i = 1
        maximum_sum = nums[0]
        length = len(nums)
        while i < length:
            if summation < 0:
                summation = nums[i]
                i += 1
                maximum_sum = max(summation, maximum_sum)
                continue
            if nums[i] > 0 or nums[i] + summation > 0:
                summation += nums[i]
                maximum_sum = max(summation, maximum_sum)
            else:
                summation = nums[i]
                i += 1
                continue
            i += 1
        return maximum_sum


def main():
    sol = Solution()
    print(sol.Max_subarray([-2, -2, 10, -5]))


if __name__ == "__main__":
    main()
