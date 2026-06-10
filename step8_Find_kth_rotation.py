'''find the kth rotation of an array
example:
Input: [1, 2, 3, 4, 5], k = 2
Output: [3, 4, 5, 1, 2]
'''
def find_kth_rotation(nums, k):
    def reverse(arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    n = len(nums)
    k = k % n #we take the modulus of k with n to handle cases where
    reverse(nums, 0, n - 1) #we reverse the entire array
    reverse(nums, 0, k - 1) #we reverse the first k elements
    reverse(nums, k, n - 1) #we reverse the remaining elements
    return nums #we return the rotated array
nums = [1, 2, 3, 4, 5]
k = 2
print(find_kth_rotation(nums, k)) #[3, 4, 5, 1, 2]
'''tc: O(n) because we are reversing the array three times
sc: O(1) because we are using constant space
'''
