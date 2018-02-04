import threading
import queue


class Produser(threading.Thread):
    def __init__(self, queue, mutex, name):
        threading.Thread.__init__(self)
        self.queue = queue
        self.mutex = mutex
        self.name = name

    def run(self):
        while True:
            self.mutex.acquire()
            while self.queue.qsize() > 5:
                self.mutex.wait()
            self.queue.put(10)
            print("The thread with name %s add element to the queue" % self.name)
            self.mutex.notify()
            self.mutex.release()


class Consumer(threading.Thread):
    def __init__(self, queue, mutex, name):
        threading.Thread.__init__(self)
        self.queue = queue
        self.mutex = mutex
        self.name = name

    def run(self):
        while True:
            self.mutex.acquire()
            while self.queue.qsize() == 0:
                self.mutex.wait()
            self.queue.get()
            print("The thread with name %s remove element from the queue" % self.name)
            self.mutex.notify()
            self.mutex.release()

queue = queue.Queue()
mutex = threading.Condition()
p1 = Produser(queue, mutex, "p1")
p2 = Produser(queue, mutex, "p2")
q1 = Consumer(queue, mutex, "q1")
q2 = Consumer(queue, mutex, "q2")
q3 = Consumer(queue, mutex, "q3")
p1.start()
p2.start()
q1.start()
q2.start()
q3.start()


