class A:
    count=0 #static parametr
    def __init__(self,a):
        self.a=a
        A.count+=1

    @staticmethod #static method
    def num_of_obj():
        return A.count

pa=A(10)
pl=A(20)
print(A.count)

