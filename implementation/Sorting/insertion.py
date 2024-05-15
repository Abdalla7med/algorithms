def insertion(arr):

    for i in range(1,len(arr)):
        key= arr[i]
        j=i-1
        while j>=0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        
    
"""
Time Complexity:
  - Average: O(n^2)
  - Worst: O(n^2)
  - Best: O(n) (already partially sorted array)

Space Complexity:
  - O(1) (in-place sorting)

Handle the result after x iterations
example 
< 4, 9, 3, 2, 6, 1, 8>
first iteration:
 key=9 and j=0
 9 < 4 false then won't enter the loop
 the result is the same
second iteration:
    key=3 and j=1
    3 < 9 True 
    swap (3,9)

    key = 3 and j=0
    3 < 4 True  swap (3,4)

    the reuslt is 
    <3, 4, 9, 2, 6, 1, 8>
Third Iteration
    key = 2 and j=2
    2 < 9 True -> swap (2,9)
    2 < 4 True -> swap (2,4)
    2 < 3 True -> swap(2,3)
    then the result is :
    <2 ,3, 4, 9, 6, 1, 8>
Fourth Iteration 
    key= 6 and j=3
    6 < 9 True swap(6,9)
    6 < 4 break
    reuslt 
    <2 ,3, 4, 6, 9, 1, 8>
Fifth iteration 
    key =1 and j=4
    1 <9
    1 < 6
    1 < 4 
    1 < 3 
    1 < 2 
    True for all previous 
    then the reuslt 
    < 1, ,2 3, 4, 6, 9, 8>

final one 
    key = 8 j=5 
    8 < 9 True swap(8,9)
    8 < 6 break 
final reuslt 
< 1, ,2 3, 4, 6, 8, 9>


"""