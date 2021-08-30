# Your function will take an integer X and multiple arrays as inputs,
# You need to filter the elements from each array that are greater than X.
# Store all the filtered elements in a new array.
# Remove duplicates
# Return the sum of all elements in the new array.


# function for calculating sum
def sumfn(arr):
    total=0
    for i in arr:
        total+=i
    return total

# function take x and multiple arguments as input
def exp2(x,*args):
    temp=[] 
    for arg in args:
        for val in arg:
            # filter elements greater than x
            if val > x and val not in temp:
                # add in the list and no duplicates
                temp.append(val)
    # return the sum of list
    return sumfn(temp)

# Run the function for given input

print(exp2(50,[10,12,34,46,55,79,80],[12,22,33,44,45,60,70,80],[9,10,120,130,140,55,199],[20,23,4,40,50,12,23,44,55] ))