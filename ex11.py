# Function to find out ways to form a string from another string.
# Function will take 2 strings as inputs. You must find out all 
# possible ways by which you can form string A from String B. You 
# must validate to ensure that the strings are Alpha-numeric only, 
# it must contain only strings and numbers. No other types are 
# allowed. The length of String B must be >er than String A.
# Char once used from String B must not be used again.
# Return the final Output in dictionary format with indexes and values.
# Indexes represent the index value in String B that has occurrence of 
# a char from String A. Function to find out ways to form a string from 
# another string. Function will take 2 strings as inputs.

def ex11(list_str1,list_str2):
    op=[]
    res={}
    for idx, val in enumerate(list_str2):
        if val in list_str1:
            res[idx]=val
        if len(res)==len(list_str1):
            op.append(res)
            res={}
    return op


# Run the function for given input
print(ex11("abc", "agcb xyzbc amnopq copnotab coscab"))

# print(ex11("ab", "agcb xyzbc amnopq copnotab coscabbb"))