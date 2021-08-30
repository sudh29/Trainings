# Your function will take multiple arrays as inputs
# For each element in each array:
# Find out how many times that element occurs in each array, store it in a dictionary.
# Sort the final dictionary based on keys and return.

# take multiple arguments as input
def exp3(*args):
    res={} # initailize empty dic
    i=0
    for arg in args:
        temp={} # intialize nested dic
        # count and add frequncy of each element in dic
        for val in arg:
            if val in temp:
                temp[val]+=1
            else:
                temp[val]=1
        # temp2 = {}
        # for j in sorted(temp):
        #     temp2[j] = temp[j]
        res[i]=temp
        i+=1
    return res

# Run the function for given input

print(exp3([12,12,55,79,79],[12,33,60,60,79],[199,55,199]))