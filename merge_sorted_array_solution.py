# Given input arrays nums1 and nums2, and their respective lengths m and n.
nums2 = [1, 2, 3]
m = 3
nums1 = [2, 5, 6, 0, 0, 0]
n = 3

# Initialize three pointers:
# p1 points to the last non-zero element in nums1
p1 = m - 1
# p2 points to the last element in nums2
p2 = n - 1
# p3 points to the last position in the merged nums1
p3 = m + n - 1

# Merge the two arrays nums1 and nums2 in non-decreasing order.
while p1 >= 0 and p2 >= 0:
    # Compare the elements at p1 and p2.
    if nums1[p1] >= nums2[p2]:
        # If the element in nums1 is greater or equal, move it to the last position (p3).
        nums1[p3] = nums1[p1]
        # Move the pointer p1 one step to the left in nums1.
        p1 -= 1
    else:
        # If the element in nums2 is greater, move it to the last position (p3).
        nums1[p3] = nums2[p2]
        # Move the pointer p2 one step to the left in nums2.
        p2 -= 1
    # Move the pointer p3 one step to the left in the merged nums1.
    p3 -= 1

# If there are remaining elements in nums2, add them to the merged array.
while p2 >= 0:
    nums1[p3] = nums2[p2]
    # Move the pointer p2 one step to the left in nums2.
    p2 -= 1
    # Move the pointer p3 one step to the left in the merged nums1.
    p3 -= 1

# Print the final merged nums1 array.
print(nums1)
