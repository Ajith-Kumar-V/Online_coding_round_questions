def divisors(integer):
    pass
    delt=[]
    for i in range(2,integer):
        if ((integer%i)==0):
            delt.append(i)
    if len(delt)==0:
        return (str(integer)+(" is prime"))
    return delt
