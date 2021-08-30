def exp2(x,*args):
    temp=[]
    for arg in args:
        for val in arg:
            if val > x and val not in temp:
                temp.append(val)
    return sum(temp)


print(exp2(50,[10,12,34,46,55,79,80],[12,22,33,44,45,60,70,80],[9,10,120,130,140,55,199],[20,23,4,40,50,12,23,44,55] ))