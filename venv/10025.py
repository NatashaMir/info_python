#process

import multiprocessing

def sum(begin, end, resultQuery):
    result = 0
    for i in range(begin, end):
        result += i
    resultQuery.put(result)

if __name__ == '__main__':
    resultQuery1 = multiprocessing.Queue()
    resultQuery2 = multiprocessing.Queue()
    process1 = multiprocessing.Process(target = sum, args = (0, 5000, resultQuery1,))
    process2 = multiprocessing.Process(target = sum, args = (5000, 10001, resultQuery2,))

    process1.start()
    process2.start()
    process1.join()
    process2.join()

    total = resultQuery1.get() + resultQuery2.get()

    print(total)
