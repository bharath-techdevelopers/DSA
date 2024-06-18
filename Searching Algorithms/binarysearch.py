def binary(l,val):
    low=0
    high=len(l)-1
    while low<=high:
        #Here we can't use len(list)//2 
        #If we use that one the 1st mid value is correct but after the condition we are moving low and high on that basis we have to change mid also
        #That means mid is changing in every iteration based on low and high
        mid=(low+high)//2
        if l[mid]==val:
            return mid
        elif l[mid]<val:#It means the value is in right side of mid so low should be moved
            low=mid+1
        elif l[mid]>val:#It means the value is in left side of the mid so high should be moved
            high=mid-1
    return -1#if the index is not found we are returning -1
l=list(map(int,input().split()))
val=int(input())
'''
1.For binary search the list elements should be sorted.
2.We have to remove duplicates also
If we didn't remove duplicates the output will be displayed based on the mid index when mid found 1st duplicate element then it returns the index but it is not correct output.
'''
l.sort()
print(l)
print(binary(l,val))#the index of val will be printed if found in sorted list else -1 will be printed
#if binary(l,val)!=-1:
    #print(f'Index of {val} is {binary(l,val)}')
#else:
    #print(f"Index not found for value {binary(l,val)}")