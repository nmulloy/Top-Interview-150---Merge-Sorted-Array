def rotate(nums, k):
    # Calculate the effective rotation (if k is greater than the length of the array)
    k = k % len(nums)

    # If the effective rotation is 0, no need to rotate
    if k == 0:
        return nums

    # Reverse the entire array
    nums.reverse()
    print(nums)

    # Reverse the first 'k' elements
    nums[:k] = reversed(nums[:k])
    print(nums[:k])

    # Reverse the remaining elements (i.e., from index k to the end)
    nums[k:] = reversed(nums[k:])
    print(nums[k:])

    return nums

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
result = rotate(nums, k)
print(result)