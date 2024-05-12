/// heap sort 
// smallest element of max heap is one of leaf nodes 
//but we can't determine which is the smallest element the only thing
// that we sure that minimum element is at last level
// k-th largest element in max-heap where 2<= k <= n/2 
/*
             16
           /    \
         14      10
        /  \    /  \
-->   8    7   9   3
14 or 8 or 10 all are k-th largest elemen but if we say 8 then at k-1 level
and if we say 10 3th at k-1 level , but 14 is 2th largest and at level 2 not k-1 
crtical but there's no rule or general formula in Trees just visualize them and then answer
*/


/*
     1
   /   \
  2     3
 / \   / \
4   5 6   7
this min-heap is sorted array 
[1,2,3,4,5,6,7]
*/

// sorting using heap sort 
/*

it is true that for storing an n-element heap, 
the leaves are the nodes indexed by ⌊n/2⌋ + 1, ⌊n/2⌋ + 2, …, n. 
This is because a heap is a complete binary tree, 
meaning that all levels are filled except possibly the last level,
 and the last level is filled from left to right. 
 Therefore, the number of internal nodes (nodes that have children) in a heap is at most ⌊n/2⌋, 
 and the number of leaf nodes (nodes that have no children) is at least n - ⌊n/2⌋. 
 The internal nodes are indexed from 1 to ⌊n/2⌋,
  and the leaf nodes are indexed from ⌊n/2⌋ + 1 to n.
*/

// heapify algorithm
/*
MAX-HEAPIFY .A; i /
1 l = LEFT(i) /
2 r = RIGHT(i) /
3 if l < A:heap-size and A[l] > A[i]
4 largest =l
5 else largest = i
6 if r < A:heap-size and A[r] > A[i]
7 largest = r
8 if largest != i
9 exchange  A[i] with A[largest]
10 MAX-HEAPIFY (A,largest)
 Complexity is O(lg n)

*/
void max_heapify(vector<int>A,int i)
{
  int largest=i;
  int l=LEFT(i);
  int r=RIGHT(i);
  if(l< A.size() && A[l] > A[i]){
    largest=l;
  }
  if(l< A.size() && A[r] > A[i]){
    largest=r;
  }
  if(largest!=i){
    swap(A[i],A[largest]);
  }
  max_heapify(A,largest);
}

void swap(int&a,int&b)
{
  int temp=a;
  a=b;
  b=temp;
}
int LEFT(int i)
{
  return i>>2;
}

int RIGHT(int i)
{
  return LEFT(i)+1;
}
/*
 starting from n/2 because leaves are good no need to heapify them

 A[1....n/2] are rooted heaps

 A[n/2+1....n] are leaves and no need to heapify them because leaves are good 
  pusedocode
  void Build_MAX_Heap(A):
    for(i=n/2 down to 1)
      max_heapify(A,i)

Complexity is 
n for loop and lg n for haepify 
 O(n*lg n)
*/

void build_max_heap(vector<int>A){
  int n=A.size();
  for(i=n/2;i>=0;i--)
      max_heapify(A,i);
}
/*
1.Buidl heap form unordered array
2.swap A[n] with A[0]
3. discard node n by decrement heap_size
4.call max_heapify(A,0)
Complexity is O(n lgn)
n for build_max_heap
n for while loop 
2n is n only
and max_heapify lg n
T(n)=nT(1)+lg n -> f(n) so T(n) is a*f(n)
*/
void heap_sort(vector<int>A,int n){
  build_max_heap(A);
  while(n--){
   swap(A[0],A[n]);
   max_heapify(A,0);
  }
}

/*
sort elment in stack using two stacks
*/

stack<int> sortStack(stack<int>st){
  stack<int>sorted,temp;
  while(!st.empty()){
    if(sorted.empty()){  
        sorted.push(st.top());
    }else{
      if(st.top()>sorted.top()){
        while(st.top()>sorted.top()){
          temp.push(sorted.top());
          sorted.pop();
        }
      }
      sortd.push(st.top());
      while(!temp.empty()){
        sorted.push(temp.top());
        temp.pop();
      }
    }
    st.pop();
  }
  return sorted;
}

/*

trace cases 
st -> 2 4 3 7 1 5 6 from bottom to top
then in first iteration 
  sorted -> 6
  temp -> empty
2. 
  sorted -> 6 5 
  temp ->empty
3. 
    sorted -> 6 5 1 
    temp -> empty
4.
    st.top() > sorted.top() then do following
    while(st.top() > sorted.top())
     temp -> 1 5 6 
    sorted -> 7
    then while(!temp.empty()):
       sorted-> 7 6 5 1
5.  3 > 1 
    while(st.top() > sorted.top())
     temp -> 1
    sorted -> 7 6 5 3
    then while(!temp.empty()):
       sorted-> 7 6 5 3 1
6.  4 > 1
    while(st.top() > sorted.top())
     temp -> 1 3  
    sorted -> 7 6 5 4
    then while(!temp.empty()):
       sorted-> 7 6 5 4 3 1
7.  2 > 1
    while(st.top() > sorted.top())
     temp -> 1
    sorted -> 7 6 5 4 3 2
    then while(!temp.empty()):
       sorted-> 7 6 5 4 3 2 1
then the sorted version of st is sortd stack with min at top 
and this is implementation of min heap using stack 
Time Complexity: best case : O(N) worst and Average Case O(n^2)
================================================================
----------------------------------------------------------------
-- note we can do this using min heap or max heap 
1. create heap --take O(n) #build_max_heap
2. delete node at 1 with node at n
3. discard node at n  by decrement heap_size
4. heapify_max (A,1)  --take O(lg n)
total time complexity O(n lgn)
   

*/




/*

Merge sort

1.Divide the unsorted array into subarray, each containing a single element.
2.Take adjacent pairs of two single-element array and merge them to form an array of 2 elements.
3.Repeat the process till a single sorted array is obtained.

An array of Size ‘N’ is divided into two parts ‘N/2’ size of each.
then those arrays are further divided till we reach a single element. 
The base case here is reaching one single element. 
When the base case is hit, we start merging the left part and the right part and we get a sorted array at the end. 
Merge sort repeatedly breaks down an array into several subarrays until each subarray consists of a single element and merging those subarrays in a manner that results in a sorted array.

Time Complexity : O(n logn)
Space Complexity : O(n)
-- note that inplace merge sort doesn't make sense (impratical )


*/
// here's a python code
int[]megresort(int[]A,int lo,int hi){
  if(lo==hi){
    return new int[A[lo]];
  }
  int mid=(lo+hi)/2;
  int[]left=megresort(A,lo,mid);
  int[]right=megresort(A,mid+1,hi);
int[]sorted=megresortedArrays(left,right);
}

int[]megresortedArrays(int[]first,int[]second){
  int n=first.length(),m=second.length();
  int[]sorted=new sorted[first.length()+second.length()];
  int j=0,i=0,k=0;
  // tow fingers approach
  while(i<=n&&j<=m){
     if(first[i]<second[j]){
      sorted[k++]=first[i++];
     }else{
      sorted[k++]=second[j++];
     }
  }
  if(i==n){
    while(i<=n){
      sorted[k++]=first[i++];
    }
  }
  if(j==m){
    while(j<=m){
    sorted[k++]=second[j++];
    }
  }
return sortd
}

// quick sort is added to binary search tree algos file
// because i wanna code it in python 
