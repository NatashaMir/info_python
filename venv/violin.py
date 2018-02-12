import threading
import queue
import time

class Violonist(threading.Thread):
    def __init__(self, queueViolin, queueBow, mutexViolin, mutexBow, name):
        threading.Thread.__init__(self)
        self.queueViolin = queueViolin
        self.queueBow = queueBow
        self.mutexViolin = mutexViolin
        self.mutexBow = mutexBow
        self.name = name

    def run(self):
        while True:
            self.mutexViolin.acquire()
            while self.queueViolin.qsize() == 0:
                self.mutexViolin.wait()
            self.queueViolin.get()
            print("The thread with name %s take the violin from the queue" % self.name)
            self.mutexViolin.notify()
            self.mutexViolin.release()

            self.mutexBow.acquire()
            while self.queueBow.qsize() == 0:
                self.mutexBow.wait()
            self.queueBow.get()
            print("The thread with name %s take the bow from the queue" % self.name)
            self.mutexBow.notify()
            self.mutexBow.release()

            print("The thread with name %s is playing" % self.name)
            time.sleep(5)

            self.mutexViolin.acquire()
            self.queueViolin.put('violin')
            print("The thread with name %s return the violin" % self.name)
            self.mutexViolin.release()

            self.mutexBow.acquire()
            self.queueBow.put('violin')
            print("The thread with name %s return the bow" % self.name)
            self.mutexBow.release()

queueViolin = queue.Queue()
queueBow = queue.Queue()
mutexViolin = threading.Condition()
mutexBow = threading.Condition()
queueViolin.put('violin')
queueViolin.put('violin')
queueViolin.put('violin')
queueBow.put('bow')
queueBow.put('bow')
queueBow.put('bow')
q1 = Violonist(queueViolin,queueBow,mutexViolin, mutexBow, "q1")
q2 = Violonist(queueViolin,queueBow,mutexViolin, mutexBow, "q2")
q3 = Violonist(queueViolin,queueBow,mutexViolin, mutexBow, "q3")
q4 = Violonist(queueViolin,queueBow,mutexViolin, mutexBow, "q4")
q5 = Violonist(queueViolin,queueBow,mutexViolin, mutexBow,"q5")
q6 = Violonist(queueViolin,queueBow,mutexViolin, mutexBow, "q6")
q1.start()
q2.start()
q3.start()
q4.start()
q5.start()
q6.start()