import threading
import random
import time

def PlayingViolinist():
    violins = [threading.Lock() for n in range(3)]
    bows  = [threading.Lock() for n in range(3)]
    violinistNames = ('First', 'Second', 'Third', 'Fourth', 'Fifth', 'Sixth')
    violinists = [Violinist(violinistNames[i], violins[i % 3], bows[i % 3]) \
                  for i in range(6)]

    random.seed(100000)
    Violinist.running = True
    for p in violinists:
        p.start()
    time.sleep(100)
    Violinist.running = False
    print("Now we're finishing.")

class Violinist(threading.Thread):

    running = True

    def __init__(self, xname, violin, bow):
        threading.Thread.__init__(self)
        self.name = xname
        self.violin = violin
        self.bow = bow

    def run(self):
        while (self.running):
            #  Violinist is waiting
            time.sleep(random.uniform(3, 15))
            print('%s want to play the violin.' % self.name)
            self.play()

    def play(self):
        violin1, bow2 = self.violin, self.bow

        while self.running:
            violin1.acquire(True)
            locked = bow2.acquire(False)
            # print(locked)
            if locked:
                break
            violin1.release()
            print('%s swaps instruments' % self.name)
            violin1, bow2 = bow2, violin1
        else:
            return

        self.playing()
        bow2.release()
        violin1.release()

    def playing(self):
        print('%s starts playing ' % self.name)
        time.sleep(random.uniform(1, 12))
        print('%s finish playing and relax.' % self.name)



PlayingViolinist()