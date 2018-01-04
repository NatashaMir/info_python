def myrange(start, end, step):
    tmp = start
    while(tmp<end):
        yield tmp
        tmp+=step


for i in myrange(0,10,2):
    print(i)
