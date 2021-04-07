import threading as t
import multiprocessing as mp
import os

result = [131]


def squareNums(l):
    # threads share same code, data and files from parent process
    for i in l:
        result.append(i * i)
    print("Result in thread: {}".format(result))


def executeThread():
    l = [1, 2, 3]
    p1 = t.Thread(target=squareNums, args=(l,))
    print(f"initial result is {result}")
    p1.start()
    p1.join()
    print(f"final result is {result}")


def executeProcess():
    l = [1, 2, 3]
    p1 = mp.Process(target=squareNums, args=(l,))
    print(f"initial result is {result}")
    p1.start()
    p1.join()
    print(f"final result is {result}")


if __name__ == "__main__":
    print("MultiProcessor:")
    executeProcess()
    print("MultiThread:")
    executeThread()

"""
thread shares the same code, data and file that of the parent process 
so if any changes in data occurs it's for the process memory space.
However in case of processes they have their own memory space and
any change in that local memory space doesn't change the value in parent memory space
"""
