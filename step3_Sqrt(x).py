def sqrt(x):
    left = 0
    right = x
    ans = 0 #we will store the answer here
    while left <= right:
        mid = left + right // 2
        square = mid * mid
        if square == x:#we found the answer
            return mid
        elif square < x:#we need to search in the right half
            left = mid + 1
            ans = mid #we store the last mid as the answer
        else:#we need to search in the left half
            right = mid - 1
    return ans #we return the last mid as the answer
#test the function
x = 4
print(sqrt(x)) #2
print(sqrt(4)) #2
print(sqrt(8)) #2
'''tc: O(log n) because we are using binary search
sc: O(1) because we are using constant space'''