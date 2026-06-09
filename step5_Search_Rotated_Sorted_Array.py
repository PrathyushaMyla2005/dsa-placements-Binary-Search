'''search for roqted sorted array
example:
Input: [4,5,6,7,0,1,2], 0
Output: 4
input: [4,5,6,7,0,1,2], 3
Output: -1'''
def search_rotated_sorted_array(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        #we need to check if the left half is sorted or not
        if nums[left] <= nums[mid]: #left half is sorted
            if nums[left] <= target < nums[mid]: #target is in the left half
                right = mid - 1
            else: #target is in the right half
                left = mid + 1
        else: #right half is sorted
            if nums[mid] < target <= nums[right]: #target is in the right half
                left = mid + 1
            else: #target is in the left half
                right = mid - 1
    return -1 #we did not find the target
#test the function
nums = [4,5,6,7,0,1,2]
target = 0
print(search_rotated_sorted_array(nums, target)) #4
'''tc: O(log n) because we are using binary search
sc: O(1) because we are using constant space
'''