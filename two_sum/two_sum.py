def twoSum(nums: list, target: int):
    sum_both = 0
    i = 0
    new_list = []
    for element1 in nums:
        flag_index = False
        for element2 in nums:
            if nums.index(element2) == nums.index(element1) and not flag_index:
                flag_index = True
                continue

            i += 1
            if i == len(nums):
                i -= 1
            if element1 + element2 == target:
                new_list.append(nums.index(element1))
                new_list.append(i)
                return new_list
        i = 0


if __name__ == "__main__":
    nums1 = [3,2,4]
    nums2 = [2,7,11,15]
    nums3 = [3,3]
    nums4 = [-10,-1,-18,-19]
    target1 = 6
    target2 = 9
    target3 = 6
    target4 = -19
    a = twoSum(nums4, target4)
    print(a)
