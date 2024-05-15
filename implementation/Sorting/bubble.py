def bubbleSort(arr):
  for i in range(len(arr) - 1):
    swapped = False
    for j in range(len(arr)-i-1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1]=arr[j + 1], arr[j]
        swapped = True
    if not swapped:
      break
"""
Time Complexity:
  - Average: O(n^2)
  - Worst: O(n^2)
  - Best: O(n) (already sorted array)

Space Complexity:
  - O(1) (in-place sorting)
"""
