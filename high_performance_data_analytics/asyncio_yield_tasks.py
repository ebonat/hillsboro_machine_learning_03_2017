
# Task1 will run independence
# Task2 needs to be run after task1 is complete finish
# Task3 needs to be run after task2 is complete finish
# Taks4 needs to be run after task1 and task3 finish
# Task5 needs to be run independence

import asyncio

async def task1():
    print('Running Task1')
    await asyncio.sleep(1)
    print('> Task1: yield to Task2')
    await task2()
    print('> Task1: yield to Task4')
    await task4()
    print('>> Task1 done!')

async def task2():
    print('Running Task2')
    await asyncio.sleep(2)
    print('> Task2: yield to Task3')
    await task3()
    print('>> Task2 done!')

async def task3():
    print('Running Task3')
    await asyncio.sleep(5)
    print('>> Task3 done!')

async def task4():
    print('Running Task4')
    await asyncio.sleep(4)
    print('>> Task4 done!')

async def task5():
    print('Running Task5')
    await asyncio.sleep(1)
    print('>> Task5 done!')

def main():
    ioloop = asyncio.get_event_loop()
    tasks = [ioloop.create_task(task1()), ioloop.create_task(task5())]
    wait_tasks = asyncio.wait(tasks)
    ioloop.run_until_complete(wait_tasks)
    ioloop.close()

if __name__ == '__main__':
    main()