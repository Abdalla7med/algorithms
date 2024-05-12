
#solution for problem Brick Blowing Problem number 4 in this session 
def get_damages(H):
    D = [1 for _ in H]
    H2 = [(H[i], i) for i in range(len(H))]
    def merge_sort(A, a = 0, b = None):
        if b is None: b = len(A)
        if 1 < b - a:
            c = (a + b + 1) // 2
            merge_sort(A, a, c)
            merge_sort(A, c, b)
            i, j, L, R = 0, 0, A[a:c], A[c:b]
            while a < b:
              if (j >= len(R)) or (i < len(L) and L[i][0] <= R[j][0]):
                D[L[i][1]] += j
                A[a] = L[i] # for keeping initial list sorted 
                i += 1
              else:
                A[a] = R[j] #for keeping initial list sorted 
                j += 1
              a += 1
    merge_sort(H2)
    return D

# Example Usage 
H=[34,57,70,19,48,2,94,7,63,75]
result=get_damages(H)
print(result) #[4, 5, 6, 3, 3, 1, 4, 1, 1, 1] works fine (done)