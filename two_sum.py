def twoSum(nums: list, target: int):
    sum_both = 0
    flag_index = False
    i = 0
    new_list = []
    for element1 in nums:
        for element2 in nums:
            if nums.index(element2) == nums.index(element1) and not flag_index:
                flag_index = True
                continue

            i += 1
            if element1 + element2 == target:
                new_list.append(nums.index(element1))
                new_list.append(i)
                return new_list


if __name__ == "__main__":
    nums = [3,3]
    target = 6
    twoSum(nums, target)
