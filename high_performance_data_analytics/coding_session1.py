
# Task1, 3 and 6 will run independence
# Task2 is done after task1 is done
# Task4 and 5 are done after taks2 is done
# Task7 is done after task3 is done
# Task8 is done after task6 is done

import asyncio

async def task1():
    print('Running Task1')
    await asyncio.sleep(1)
    print('>> Task1 done!') 
    await task2()    
    
async def task2():
    print('Running Task2')
    await asyncio.sleep(8)
    print('>> Task2 done!')  
    await task4()
    await task5()
        
async def task3():
    print('Running Task3')
    await asyncio.sleep(3)
    print('>> Task3 done!')
    await task7()
    
async def task4():
    print('Running Task4')
    await asyncio.sleep(4)
    print('>> Task4 done!')

async def task5():
    print('Running Task5')
    await asyncio.sleep(1)
    print('>> Task5 done!')
    
async def task6():
    print('Running Task6')
    await asyncio.sleep(1)
    print('>> Task6 done!')
    await task8()

async def task7():
    print('Running Task7')
    await asyncio.sleep(1)
    print('>> Task7 done!')
    
async def task8():
    print('Running Task8')
    await asyncio.sleep(1)
    print('>> Task8 done!')
    
def main():
    ioloop = asyncio.get_event_loop()
    tasks = [ioloop.create_task(task1()), ioloop.create_task(task3()), ioloop.create_task(task6())]
    wait_tasks = asyncio.wait(tasks)
    ioloop.run_until_complete(wait_tasks)
    ioloop.close()

if __name__ == '__main__':
    main()