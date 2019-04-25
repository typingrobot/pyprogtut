import threading
import time
import multiprocessing


def countdown():
    x = 100000000
    while x > 0:
        x -= 1


# Implementation 1 - multi-threading
def implementation_1():
    thread_1 = threading.Thread(target=countdown)
    thread_2 = threading.Thread(target=countdown)
    thread_3 = threading.Thread(target=countdown)
    thread_4 = threading.Thread(target=countdown)
    thread_1.start()
    thread_2.start()
    thread_3.start()
    thread_4.start()
    thread_1.join()
    thread_2.join()
    thread_3.join()
    thread_4.join()


# Implementation 2 - run in serial
def implementation_2():
    countdown()
    countdown()
    countdown()
    countdown()


# Implementation 3 - multi-process
def implementation_3():
    process_1 = multiprocessing.Process(target=countdown)
    process_2 = multiprocessing.Process(target=countdown)
    process_3 = multiprocessing.Process(target=countdown)
    process_4 = multiprocessing.Process(target=countdown)
    process_1.start()
    process_2.start()
    process_3.start()
    process_4.start()
    process_1.join()
    process_2.join()
    process_3.join()
    process_4.join()


start = time.time()
implementation_1()
end = time.time()
print(end - start)

start = time.time()
implementation_2()
end = time.time()
print(end - start)

start = time.time()
implementation_3()
end = time.time()
print(end - start)
