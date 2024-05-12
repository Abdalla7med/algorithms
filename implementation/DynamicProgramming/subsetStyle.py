"""
def LIS(List):
    n =len(List)
    memo={}
    def helper(i,prev):
        if i==n:
            return 0

        if (i,prev) in memo:
            return memo[(i,prev)]

        ch1=helper(i+1,prev)
        ch2=0
        if List[prev] <= List[i]:
            ch2=helper(i+1,i)+1
        memo[(i,prev)]=max(ch1,ch2)
        return memo[(i,prev)]
    return helper(0,n-1) # start with no prev 
# Example
list={5,2,7,3,4,6}
print(LIS(list))

"""
def LIS(List):
    n = len(List)
    memo = {}  # Memoization table to store computed results
    
    def helper(i, prev):
        if i == n:
            return 0
        
        if (i, prev) in memo:  # If result for current state is already computed, return it
            return memo[(i, prev)]
        
        ch1 = helper(i + 1, prev)  # Exclude the current element
        ch2 = 0  # Include the current element if it's greater than the previous element
        if prev == -1 or List[i] > List[prev]:
            ch2 = 1 + helper(i + 1, i)
        
        memo[(i, prev)] = max(ch1, ch2)  # Store the computed result in memoization table
        return memo[(i, prev)]
    
    return helper(0, -1) if n > 0 else 0  # Start with index 0 and no previous element (-1), or return 0 for empty list


# Example usage:
arr = [10, 22, 9, 33, 21, 50, 41, 60]
print(LIS(arr))  # Output: 5 (for the LIS: [10, 22, 33, 50, 60])

empty_arr = []
print(LIS(empty_arr))  # Output: 0 (for an empty list)

#Longest Common subsquence between two strings 

def LCS(str1, str2):
    def helper1(i,j):
        if i==len(str1) or j==len(str2):
            return 0
        if str1[i]==str2[j]:
            return 1+helper1(i+1,j+1)
        ch1=helper1(i+1,j)
        ch2=helper1(i,j+1)
        return max(ch1,ch2)
    return helper1(0,0)
#usage 
str1="abcdefgzh"
str2="ackghefhlmn"
print(LCS(str1,str2))
