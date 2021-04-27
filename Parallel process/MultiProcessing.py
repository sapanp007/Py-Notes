# CPU bound tasks

import multiprocessing
import os

l = [1, 2, 3, 4]


def func1(l):
    print(f"Inside func1 and process id : {os.getpid()} and number: {l}")


"""RuntimeError:
        An attempt has been made to start a new process before the
        current process has finished its bootstrapping phase."""
# p1 = multiprocessing.Process(target=func1, )
# p1.start()
# p1.join()
if __name__ == "__main__":
    p1 = multiprocessing.Process(target=func1, args=(l,))
    p1.start()
    print(f"p1 = {p1.pid} and __main__ = {os.getpid()}")
    p1.join()

"""Sharing of data between multiple processes can be achieved by 2 ways: 
# 1.using global keyword
# 2.using shared memory(Array and Value objects)"""

"""using global keyword"""
import multiprocessing as mp

result = [131]


def squareNums(l):
    global result  # creates a copy of result in p1 memory space
    print(f"initial result in squarenums is {result}")
    for i in l:
        result.append(i * i)
    print("Result(in process p1): {}".format(result))


if __name__ == "__main__":
    l = [1, 2, 3]
    p1 = mp.Process(target=squareNums, args=(l,))
    print(f"initial result is {result}")
    p1.start()
    p1.join()
    print(f"final result is {result}")

"""2.using shared memory(Array and Value objects)"""
import multiprocessing as mp


def func1(l, total_sum, sq_arr):
    for idx, num in enumerate(l):
        sq_arr[idx] = num * num
    total_sum.value = sum(l)


if __name__ == "__main__":
    l = [1, 2, 4, 5]
    total_sum = mp.Value('i')
    sq_arr = mp.Array('i', 4)
    p1 = mp.Process(target=func1, args=(l, total_sum, sq_arr,))
    p1.start()
    p1.join()
    print(sq_arr[:], total_sum.value)

"""Server process : Whenever a python program starts, a server process is also started. From there on, 
whenever a new process is needed, the parent process connects to the server and requests it to fork a new process.
A server process can hold Python objects and allows other processes to manipulate them using proxies.
multiprocessing module provides a Manager class which controls a server process. Hence, 
managers provide a way to create data which can be shared between different processes."""
import multiprocessing as mp


def _insert(records, record):
    records.append(record)


def _print_records(records):
    print(records)


if __name__ == "__main__":
    manager = mp.Manager()
    records = manager.list([1, 2, 3, 4])
    p1 = mp.Process(target=_insert, args=(records, 1,))
    p2 = mp.Process(target=_print_records, args=(records,))
    p1.start()
    p1.join()
    p2.start()
    p2.join()
    print(dir(manager))

"""multiprocessing supports two types of communication channel between processes:
Queue
Pipe
"""
import multiprocessing as mp


def square_list(l, q):
    for i in l:
        q.put(i * i)


def print_queue(q):
    while not q.empty():
        print(q.get())


if __name__ == "__main__":
    l = [1, 2, 4, 5]
    q = mp.Queue()
    p1 = mp.Process(target=square_list, args=(l, q,))
    p2 = mp.Process(target=print_queue, args=(q,))
    p1.start()
    p1.join()
    p2.start()
    p2.join()

"""Synchronization and Pooling of processes in Python"""
import multiprocessing as mp


def deposit(amount):
    for _ in range(100000):  # differnce won't be noticed if performed for less times like 100
        amount.value = amount.value + 10


def withdraw(amount):
    for _ in range(100000):
        amount.value = amount.value - 10


def transaction():
    amount = mp.Value('i', 100)
    p1 = mp.Process(target=deposit, args=(amount,))
    p2 = mp.Process(target=withdraw, args=(amount,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(f"final balance: {amount.value}")


if __name__ == "__main__":
    for _ in range(10):
        transaction()
"""Output:
final balance: 670
final balance: 43330
final balance: -17990
final balance: 51370
final balance: 35570
final balance: 88960
final balance: -79820
final balance: 17840
final balance: 54670
final balance: 68970"""

"""use locking """
import multiprocessing as mp


def deposit(amount, lock):
    for _ in range(100000):  # differnce won't be noticed if performed for less times like 100
        lock.acquire()
        amount.value = amount.value + 10
        lock.release()


def withdraw(amount, lock):
    for _ in range(100000):
        lock.acquire()
        amount.value = amount.value - 10
        lock.release()


def transaction():
    amount = mp.Value('i', 100)
    lock = mp.Lock()
    p1 = mp.Process(target=deposit, args=(amount, lock,))
    p2 = mp.Process(target=withdraw, args=(amount, lock,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(f"final balance: {amount.value}")


if __name__ == "__main__":
    for _ in range(10):
        transaction()

"""Pooling"""
import multiprocessing, os


def sq_num(n):
    print(f"pid - {os.getpid()} and n is :{n}")
    return n * n


if __name__ == "__main__":
    l = range(100000)
    p = multiprocessing.Pool()
    result = p.map(sq_num, l)
"""
Output:
pid - 27372 and n is :93747
pid - 27372 and n is :93748
pid - 27372 and n is :93749

pid - 28592 and n is :96839
pid - 28592 and n is :96840
pid - 28592 and n is :96841
pid - 28592 and n is :96842
"""

"""
How pooling works?
https://www.ellicium.com/python-multiprocessing-pool-process/
"""

"""if number of processes needed are less (eg. 10 or 100) then better to use processes list else pool class
#for less args:
processes = []
for _ in range(10):
    p = mp.Process(target=func1,args=(arg1,))
    processes.append(p)
    p.start()
for p in processes:
    p.join()
"""
