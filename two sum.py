from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        # two pointer technique with sorting -> time -> O(nlogn)
        # hashing technique -> time -> O(n)
        di = {}
        for i in range(len(nums)):
            if target - nums[i] in di:
                return [di[target - nums[i]], i]
            else:
                di[nums[i]] = i
        # no need we will find solution in loop itself acc. to the question


if __name__ == '__main__':
    sol =Solution()
    print(sol.two_sum([1,2,3,4,5],6))
