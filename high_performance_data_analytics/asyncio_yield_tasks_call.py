import asyncio

from asyncio_yield_tasks_class import AsyncioYieldTasks

def main():
    asyncio_yield_tasks = AsyncioYieldTasks()

    ioloop = asyncio.get_event_loop()
    tasks = [ioloop.create_task(asyncio_yield_tasks.task1()), ioloop.create_task(asyncio_yield_tasks.task5())]
    wait_tasks = asyncio.wait(tasks)
    ioloop.run_until_complete(wait_tasks)
    ioloop.close()

if __name__ == '__main__':
    main()