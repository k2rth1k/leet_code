def next_permutation(nums: [int]) -> [int]:
    j = 0
    arr = []
    length = len(nums)
    for num in nums:
        arr.append(get_position(nums[j:]) - 1)
        j += 1
    arr.reverse()
    i = 1
    carry = 1
    n_arr = [0]
    while i < length and carry == 1:
        sum = arr[i] + carry
        carry = sum // (i + 1)
        n_arr.append(sum % (i + 1))
        i += 1
    n_arr.extend(arr[i:])
    arr.reverse()
    n_arr.reverse()
    result = []
    for pos in n_arr:
        nums.sort()
        result.append(nums.pop(pos))
    return result


def get_position(nums: [int]):
    j = nums[0]
    pos = 0
    for num in nums:
        if j >= num:
            pos += 1
    return pos


if __name__ == '__main__':
    print(next_permutation([1, 1, 5, 2, 3, 2, 1]))
    pass
