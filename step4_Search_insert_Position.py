'''find the position to insert the target in a sorted array
example:
Input: [1,3,5,6], 5
Outputr: 2'''
def search_insert_position(nums, target):

    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left
#test the function
nums = [1,3,5,6]
target = 5
print(search_insert_position([1,3,5,6], 5)) #2
'''tc: O(log n) because we are using binary search
sc: O(1) because we are using constant space'''
