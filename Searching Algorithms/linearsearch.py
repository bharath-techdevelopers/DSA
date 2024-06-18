def linear(l,val):
    for ind in range(len(l)):
        if l[ind]==val:
            return ind
    return -1
l=list(map(int,input().split()))#Taking the list of elements in the form of single line as 1 2 3 4..etc
val=int(input())#value to find the index 
print(linear(l,val))#print index if found and index is not found then -1 will print
#if linear(l,val)!=-1:
    #print(f'Index of {val} is {linear(l,val)}')
#else:
    #print(f"Index not found for value {linear(l,val)}")