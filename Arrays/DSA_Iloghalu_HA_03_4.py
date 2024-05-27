# Exercise 1:
# function to sort an array and find the three largest elemnts
def find_largest_three_elements(arr):
    if len(arr) < 3:
        return "Array size should be at least 3"
    arr.sort()
    find_largest_three_elements = arr[-3:]
    return find_largest_three_elements
arr = [10,50,60,3,5,2,8]
print("Original Array : ", arr)
print("The largest three elemets are: ", find_largest_three_elements(arr))
print("----------------------------------------------------")
# Exercise 2:
#function to push all the zeros in an array to the end of the arry
def push_zeros_to_end(arr):
    # Initializing a pointer to keep track of the position
    # where the next non-zero element should be placed
    next_non_zero = 0
    
    # Iterating through the array
    for i in range(len(arr)):
        # If the current element is non-zero
        if arr[i] != 0:
            # Swaping the current element with the element at the next_non_zero position
            arr[i], arr[next_non_zero] = arr[next_non_zero], arr[i]
            # Moving the next_non_zero pointer to the next position
            next_non_zero += 1
    
    return arr

# Example usage:
arr = [0, 3, 0, 4, 5, 0, 7, 0, 9]
print("Original array:", arr)
arr = push_zeros_to_end(arr)
print("Array after pushing zeros to end:", arr)
print("----------------------------------------------------")
# Exercise 3:
# function to sort array positve intergers and rearranging the array
#such that the first elemnt should be a max value, second position is min value,
#third position second max, & fourth positio second min and so on...
def rearrange_alternately(arr):
    n = len(arr)
    result = [0] * n
    left = 0  # Pointer to traverse from the left end of the array
    right = n - 1  # Pointer to traverse from the right end of the array
    for i in range(n):
        if i % 2 == 0:
            result[i] = arr[right]
            right -= 1
        else:
            result[i] = arr[left]
            left += 1
    return result

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Original array:", arr)
result = rearrange_alternately(arr)
print("Array rearranged alternately:", result)
print("----------------------------------------------------")

#Exercise 4:
#function to segegarte even and odd numbers in the given array such that even numbers 
# coms first followed by odd numbers
def segregate_even_odd(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        # Moving left pointer until it points to an odd number
        while arr[left] % 2 == 0 and left < right:
            left += 1
        # Moving right pointer until it points to an even number
        while arr[right] % 2 != 0 and left < right:
            right -= 1
        # Swap the elements pointed by left and right pointers
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

# Example usage:
arr = [12, 34, 45, 9, 8, 90, 3,7,11,4,8,20]
print("Original array:", arr)
segregate_even_odd(arr)
print("Array after segregating even and odd numbers:", arr)
