class Devided_by_zero(Exception):
    pass

def devided(a, b):
    if b == 0:
        raise Devided_by_zero()
    return a/b

#result = devided(10, 0)

try:
    result = devided(10, 0)
    print("Ok")
except Devided_by_zero as e:
    print("Error")
except Exception as e:
    print("Exception")
finally:
    print("Finally")