def removeElement(nums, val):
    # Initialize two pointers, p1 and p2, to 0.
    p1 = 0
    p2 = 0

    # Iterate through the nums list using pointer p1.
    while p1 < len(nums):
        # If the current element at index p1 is not equal to val,
        # update the element at index p2 with the value at index p1.
        if nums[p1] != val:
            nums[p2] = nums[p1]
            # Increment p2 to move to the next position to store the next non-val element.
            p2 += 1
        # Move to the next element in the nums list.
        p1 += 1

    # At the end of the loop, p2 will represent the number of elements in nums
    # that are not equal to val. Return p2 as the result.
    return p2

# Example usage:
nums = [3, 2, 2, 3, 1, 5, 3, 6]
val = 3

# Call the removeElement function with nums and val as arguments.
k = removeElement(nums, val)

# Print the number of elements in nums that are not equal to val (k).
print("k:", k)

# Print the modified nums array containing only elements that are not equal to val.
# The modified array is obtained by slicing the first k elements from nums.
print("Array:", nums[:k])
