
class Element:
    def __init__(self, key):
        self.key = key

def direct_access_sort(A):
    "Sort A assuming items have distinct non-negative keys"
    u = 1 + max([x.key for x in A])  # O(n) find maximum key
    D = [None] * u  # O(u) direct access array
    for x in A:  # O(n) insert items key 0 will be in index 0 just like frequencey array in c
        D[x.key] = x
        
    i = 0
    for key in range(u):  # O(u) read out items in order
        if D[key] is not None:
            A[i] = D[key]
            i += 1

def countingSort(arr):
    size = len(arr)
    output = [0] * size
    # first step is to find maximum element in the input array 
    # then initialize count array with size of maximum element with 0
    k=arr[0]
    for i in range(1,size):
        if arr[i]>k:
            k=arr[i]
    # count array initialization
    count = [0] * (k+1)

    # storing the count of each element 
    for m in range(0, size):
        count[arr[m]] += 1

    # storing the cumulative count
    for m in range(1, k+1):
        count[m] += count[m - 1]

    # place the elements in output array after finding the index of each element of original array in count array
    m = size - 1
    while m >= 0:
        output[count[arr[m]] - 1] = arr[m]
        count[arr[m]] -= 1
        m -= 1

    for m in range(0, size):
        arr[m] = output[m]


# def RadixSort(arr):

# Example usage
#A = [Element(5), Element(2), Element(7), Element(0), Element(4)]
#direct_access_sort(A)
#print([x.key for x in A])
    #   0 1 2 3 4 5 6   -> size is 6 
data = [0,3,4,5,7,8,14]
countingSort(data)
print("Sorted Array: ")
print(data)

"how to sort if u is less than n^2 this will be cost with previous algorithm"




