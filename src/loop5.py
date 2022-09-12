# SuperFastPython.com
# example of a parallel for loop with the Pool class
from multiprocessing import Pool

# execute a task
def task(value):
    # add your work here...
    # ...
    # return a result, if needed
    return value

# protect the entry point
if __name__ == '__main__':
    # create the pool with the default number of workers
    with Pool() as pool:
        # issue one task for each call to the function
        for result in pool.map(task, range(100)):
            # handle the result
            print(f'>got {result}')
    # report that all tasks are completed
    print('Done')
