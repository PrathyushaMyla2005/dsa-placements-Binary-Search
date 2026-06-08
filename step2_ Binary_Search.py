'''binary search is a searching algorithm used in sorted arrays. It works by repeatedly dividing the search interval in half until the target value is found or the search interval is empty.
Input: arr = [1,2,3,4,5], x = 3
Output: 2 (index of x in arr)'''
def binary_search(arr, x):
    left = 0 #Initialize the left pointer to the start of the array
    right = len(arr) - 1 #Initialize the right pointer to the end of the array
    while left <= right: #continue searching while the left pointer is less than or equal to the right pointer
        mid = left + right // 2 #Calculate the middle index
        if arr[mid] == x: #If the middle element is equal to x, return the index
            return mid
        elif arr[mid] < x: #If the middle element is less than x, move the left pointer to mid + 1
            left = mid + 1
        else: #If the middle element is greater than x, move the right pointer to mid - 1
            right = mid - 1
    return -1 #If x is not found in the array, return -1
#Example usage
arr = [1,2,3,4,5]
x = 3
print(binary_search(arr, x))
'''tc O(log n) where n is the length of the input array, as we are
halving the search space in each iteration.
sc O(1) as we are using only a constant amount of extra space for the pointers
and variables.'''