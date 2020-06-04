def linear_search(arr, target):
    # Your code here
    for x in range(len(arr)):        
        if arr[x] == target:
            return x

    return -1    


# Write an iterative implementation of Binary Search
def binary_search(arr, target):     
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right)
         
        if arr[mid] == target:
            return mid        
        
        if arr[mid] < target:            
            left = mid + 1         
        else:             
            right = mid - 1
    
    return -1 
