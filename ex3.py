def exp3(*args):
    res={}
    for arg in args:
        for val in arg:
            if val in res:
                res[val]+=1
            else:
                res[val]=1
    sres={}
    for i in sorted(res):
        sres[i]=res[i]
    return sres


print(exp3([12,12,55,79,79],[12,33,60,70,79],[12,199,55,199]))