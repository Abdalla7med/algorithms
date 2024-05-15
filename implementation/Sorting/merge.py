
def mergeSort(arr):
    if len(arr) <=1:
        return arr # already sorted 
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    merged = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i = i + 1
        else:
            merged.append(right[j])
            j = j + 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

"""
Time Complexity:
  - Average: O(n log n)
  - Worst: O(n log n) (all cases)

Space Complexity:
  - O(n) (due to recursion)
To Handle Trace 
just keep divide the arry into two arrays untill reaching base case
then merge them in sorted order (comparsion done in merge sub-routine not in sub-routine divide)

                [8, 4, 2, 1]                [7, 3, 6, 5]
                /           \               /          \
            [8, 4]        [2, 1]        [7, 3]        [6, 5]
            /     \        /     \     /     \        /     \
            [4]    [8]   [2]     [1] [3](left) [7](right)     [6]      [5]
merge      [4,8]            [1,2]         [3,7]             [5,6]
            [1,2,4,8]                   [3,5,6,7]
        [1,2,3,4,5,6,7,8]

       Merge (left, right)

          [3, 4, 5, 6, 7, 8]

"""