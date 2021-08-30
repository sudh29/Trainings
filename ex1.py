def find_remainder(X,arr):
    max_rem=arr[0]%X
    for i in arr:
        max_rem=max(max_rem,i%X)

    min_rem=max_rem
    for i in arr:
        if i%X>0 :
            temp=i%X
            min_rem=min(temp,min_rem)
    return max_rem,min_rem



x=10
array=[10,20,30,40,50,44,55,60]

print(find_remainder(x,array))