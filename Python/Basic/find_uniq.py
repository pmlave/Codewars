# find_uniq will return the unique number from a list of numbers. 
# For example, [1, 1, 1, 0, 1, 1, 1, 1] will return 0.
def find_uniq(arr):
    av = sum(arr)/len(arr)
    return max(arr) if arr[0] <= av and arr[1] <= av else min(arr)