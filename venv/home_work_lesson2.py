def mydecorator(c, d, r):
    def func_wrapper(func):
        def wrapper(a,b):
            print('decorator')
            result = 0
            if(a>c and a<d):
                if(b>c and b<d):
                    result=func(a,b)
            return result
        return wrapper
    return func_wrapper

@test(10,10,20)
def f(a, b):
    return a+b



#result = f(100, 200)
wrap1 = mydecorator(0,10)
wrap2 = wrap1(f)
result=wrap2(100, 200)
print(result)