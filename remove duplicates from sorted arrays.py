def removeDuplicates(nums):
    # Check if the input list is empty
    if not nums:
        return 0

    k = 0  # Represents the index of the last unique element found

    # Start iterating through the array from the second element (index 1)
    for i in range(1, len(nums)):
        # If the current element is different from the element at index k,
        # it means we found a new unique element.
        if nums[i] != nums[k]:
            k += 1  # Increment the index of the last unique element found
            # Move the new unique element to the position k+1 in the array,
            # effectively removing duplicates in-place.
            nums[k] = nums[i]

    # The number of unique elements is k+1 (since array indices are zero-based)
    # Return the count of unique elements.
    return k + 1

# Example usage:
nums = [1, 1, 2, 2, 2, 3, 4, 4, 5]
result = removeDuplicates(nums)
print(result)  # Output: 5
print(nums[:result])  # Output: [1, 2, 3, 4, 5]