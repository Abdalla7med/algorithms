

def left(i):
    return 2*i


def right(i):
    return 2*i + 1


def parent(i):
    return i//2


def max_heapify(a, heap_size, i):
    l = left(i)
    r = right(i)

    largest = i 

    if l < heap_size and a[l] > a[i]:
        largest = l
    
    if r < heap_size and a[r] > a[largest]:
        largest = r 
    
    if largest != i:
        # swap elements
        a[i], a[largest] = a[largest], a[i]
        max_heapify(a, heap_size, largest)


"""
Iterative Version 
def Max_heapify(self,i):
        left=2*i+1
        right=2*i+2
        while ((left < len(self.Heap) and self.Heap[i] < self.Heap[left]) or (right < len(self.Heap) and self.Heap[i] < self.Heapp[right])):
            biggest= left if (right >= len(self.Heap) or self.Heap[left] > self.Heap[right]) else right
            self.Heap[i], self.Heap[biggest] = self.Heap[biggest], self.Heap[i]

            i=biggest
            left = 2*i+1
            right= 2*i+2
"""


def build_max_heap(a):
    heap_size = len(a)

    # from the middle and go to backward throught the begining 
    for i in range(heap_size//2, 0, -1):
        max_heapify(a, heap_size, i)


def heap_sort(a):
    build_max_heap(a)

    for i in range(len(a)-1, 1, -1):
        # swap elements
        a[i], a[1] = a[1], a[i]

        # after the swap the last element is now sorted, but the new root may break the max-heap condition
        # fix it by calling max-heapify with a smaller heap size (sorted elements are out of the picture)
        
        max_heapify(a, i, 1) # pass i as size instead of modify list by pop last element 
        # just simulate that the last element is been deleted 


def main():
    
    # the root is at Index one not zero 
    # for more about way use one indexing not zero
    # https://stackoverflow.com/questions/22900388/why-in-a-heap-implemented-by-array-the-index-0-is-left-unused
    a = [None, 99, 0, 5, 20, 123, 0, -1, 72, 21, 22, 13, 8, 7, 67, 29, 1, 2, 4]
    heap_sort(a)
    print(a[1:])

    a = [None, 3, 9, 2, 1]
    heap_sort(a)
    print(a[1:])


main()

"""
Characteristics of Heapsort
Time Complexity : O (n lgn) -> merge sort inherited
Space Complexity : O(1) -> insertion sort ( in-place ) sorting inherited 

so, HeapSort combine both useful attributes of merge and insertion sort
"""