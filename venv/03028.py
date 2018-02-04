import threading

class Sum(threading.Thread):
    def __init__(self, begin, end):
        threading.Thread.__init__(self)
        self.begin = begin
        self.end = end
        self.result = 0

    def run(self):
        for i in range(self.begin, self.end):
            self.result += i

thread1 = Sum(1, 5000)
thread2 = Sum(5000, 10001)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
total = thread1.result + thread2.result
print(total)