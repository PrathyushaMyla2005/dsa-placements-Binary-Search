'''find the peak element in an array
example: [1, 3, 20, 4, 1, 0] -> 20
'''
def find_peak_element(nums):
    left = 0 #initialize left pointer
    right = len(nums) - 1 #initialize right pointer
    while left < right:
        mid = left + right // 2 #calculate the middle index
        if nums[mid] < nums[mid + 1]: #if the middle element is less than the next element, then the peak is in the right half
            left = mid + 1
        else: #if the middle element is greater than or equal to the next element, then the peak is in the left half
            right = mid
    return nums[left] #we return the peak element
#test the function
nums = [1, 3, 20, 4, 1, 0]
print(find_peak_element(nums)) #20
'''tc: O(log n) because we are using binary search
sc: O(1) because we are using constant space
'''
