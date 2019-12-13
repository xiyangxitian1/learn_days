import time
import threading
import multiprocessing


def foo():
    start = time.time()
    a = 1
    b = 3
    for i in range(10000000):
        a += i
        b -= i
    print(multiprocessing.current_process().name, threading.current_thread().name, "共用时：", time.time() - start)


if __name__ == '__main__':
    threading.Thread(target=foo).start()
    threading.Thread(target=foo).start()
    # threading.Thread(target=foo).start()
    # threading.Thread(target=foo).start()
    # threading.Thread(target=foo).start()
    # foo()
    # multiprocessing.Process(target=foo).start()
    # multiprocessing.Process(target=foo).start()
    # multiprocessing.Process(target=foo).start()
    # multiprocessing.Process(target=foo).start()
