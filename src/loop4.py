# SuperFastPython.com
# example of a parallel for loop with the Process class
from multiprocessing import Process

# execute a task
def task(value):
    # add your work here...
    # ...
    # all done
    print(f'.done {value}', flush=True)

# protect the entry point
if __name__ == '__main__':
    # create all tasks
    processes = [Process(target=task, args=(i,)) for i in range(20)]
    # start all processes
    for process in processes:
        process.start()
    # wait for all processes to complete
    for process in processes:
        process.join()
    # report that all tasks are completed
    print('Done')
