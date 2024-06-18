def interpolation(l,val):
    low=0
    high=len(l)-1
    while low<=high and l[low]<=val<=l[high]:
        ind=int(low+((low-high)/(l[low]-l[high]))*(val-l[low]))
        if l[ind]==val:
            return ind
        elif l[ind]>val:
            high=ind-1
        elif l[ind]<val:
            low=ind+1
    return -1
l=list(map(int,input().split()))#It takes input as 1 2 3 and gives output as[1,2,3]
val=int(input())
l.sort()#for this search the elements must be sort and no duplicates
print(interpolation(l,val))
#if interpolation(l,val)!=-1:
    #print(f'Index of {val} is {interpolation(l,val)}')
#else:
    #print(f"Index not found for value {binary(l,val)}")