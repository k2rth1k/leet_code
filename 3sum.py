"""
    ref:https://leetcode.com/problems/3sum/
"""


def three_sum(nums: [int]):
    length = len(nums)
    result = []
    for j in range(length):
        if length - j >= 3:
            arr = two_sum(nums[j + 1:], 0 - nums[j])
            if len(arr) != 0:
                for ar in arr:
                    ar.append(nums[j])
                    ar.sort()
                    result.append(ar)
    i = 0
    j = 0
    while i < len(result):
        j = i + 1
        while j < len(result):
            if result[i] == result[j]:
                result.pop(j)
            else:
                j += 1
        i += 1
    result.sort()
    return result


def two_sum(nums: [int], summation) -> [[int]]:
    mapper = {}
    result = []
    for ele in nums:
        if ele in mapper:
            result.append([summation - ele, ele])
        mapper[summation - ele] = True
    return result


if __name__ == '__main__':
    print(three_sum([3, -1, 2, 0, 1, -1, -2, 2, 0, -4]))
