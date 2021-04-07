# import multiprocessing
# print(multiprocessing.cpu_count())

import concurrent.futures
import time


def do_sleep(sec):
    print(f"sleeping for {sec} sec")
    time.sleep(sec)
    return f"done sleepng for {sec}"


with concurrent.futures.ThreadPoolExecutor() as executor:
    # submit indivisually
    f1 = executor.submit(do_sleep, 4)
    f2 = executor.submit(do_sleep, 5)
    print(f1.result())
    print(f2.result())

    # submit using list comp
    result = [executor.submit(do_sleep, 5) for _ in range(5)]
    for i in concurrent.futures.as_completed(result):
        print(i.result())

    # pass different arguments
    secs = [5, 4, 3, 2, 1]
    result = [executor.submit(do_sleep, sec) for sec in secs]
    for i in concurrent.futures.as_completed(result):
        print(i.result())
    """ if we give max_workers=4 the it will start for 5,4,3,2 and then start 1 sec sleep once 2sec sleep is done"""

    # using map(easy way)
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_sleep, secs)
    for result in results:
        print(result)  # handle exception here

    """
    use map if return is needed to get in the order of item execution
    use as_completed if retun is needed as soon as a future instance gets completed
    """
    """
    Advantage of using context manager during concurrent.futures is 
    we nologer need to add join or as_completed methods to wait for processes to finish
    context manager waits for all the processes to finish 
    """

"""Use of ThreadPoolExecutor"""
t1 = time.perf_counter()
with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [1, 2, 3, 4, 5]
    results = executor.map(do_sleep, secs)
    for result in results:
        print(result)
t2 = time.perf_counter()
print(f"total time taken for multithreading {t2 - t1}")
