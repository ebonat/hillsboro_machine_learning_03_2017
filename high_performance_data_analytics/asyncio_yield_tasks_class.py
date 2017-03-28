import asyncio

class AsyncioYieldTasks(object):

    def __init__(self):
        pass
        
    async def task1(self):
        print('Running Task1')
        await asyncio.sleep(1)
        print('> Task1: yield to Task2')
        await self.task2()
        print('> Task1: yield to Task4')
        await self.task4()
        print('>> Task1 done!')
    
    async def task2(self):
        print('Running Task2')
        await asyncio.sleep(2)
        print('> Task2: yield to Task3')
        await self.task3()
        print('>> Task2 done!')
    
    async def task3(self):
        print('Running Task3')
        await asyncio.sleep(5)
        print('>> Task3 done!')
    
    async def task4(self):
        print('Running Task4')
        await asyncio.sleep(4)
        print('>> Task4 done!')
    
    async def task5(self):
        print('Running Task5')
        await asyncio.sleep(1)
        print('>> Task5 done!')