
# Task4 after 1, 2 and 3 are complete done!

import asyncio

async def task1():
    print('Running Task1')
    await asyncio.sleep(3)
    print('>> Task1 done!') 
    
async def task2():
    print('Running Task2')
    await asyncio.sleep(2)
    print('>> Task2 done!')  
        
async def task3():
    print('Running Task3')
    await asyncio.sleep(5)
    print('>> Task3 done!')
    await task4()
    
async def task4():
    print('Running Task4')
    await asyncio.sleep(1)
    print('>> Task4 done!')
    
def main():
    ioloop = asyncio.get_event_loop()
    tasks = [ioloop.create_task(task1()), ioloop.create_task(task2()), ioloop.create_task(task3())]
    wait_tasks = asyncio.wait(tasks)
    ioloop.run_until_complete(wait_tasks)
    ioloop.close()

if __name__ == '__main__':
    main()