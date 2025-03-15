# def three_sum(nums):
#     result = []
#     seen = {}
#     for i, num in enumerate(nums):
#         complement = -num
#         for j in range(i+1, len(nums)):
#             remaining = complement - nums[j]
#             if remaining in seen and seen[remaining] == i:
#                 triplet = [num, nums[j], remaining]
#                 triplet.sort()
#                 if triplet not in result:
#                     result.append(triplet)
#         seen[num] = i
#     return result



def contains_duplicate(nums):
    nums.sort()  
    left, right = 0, len(nums) - 1

    while left < right:
        if nums[left] == nums[right]:
            return True
        elif nums[left] < nums[right]:
            left += 1
        else:
            right -= 1

    return False



def contains_duplicate(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False