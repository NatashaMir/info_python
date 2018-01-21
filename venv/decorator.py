def test(*decorator_arg):
    def my_decorator(func):

        def wrapped(function_arg1, function_arg2):

            for i in range(len(decorator_arg)):
                print(i)
                if func(decorator_arg[i - 1][0], decorator_arg[i - 1][1]) == decorator_arg[i - 1][2]:
                    print("Test OK!")
                else:
                    print("Test fails!")

        return wrapped

    return my_decorator


@test([10, 20, 30], [20, 30, 60])
def func(a, b):
    return a + b


func(0, 0)