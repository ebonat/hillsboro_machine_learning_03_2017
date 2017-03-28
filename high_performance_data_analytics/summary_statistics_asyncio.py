
import asyncio
import time
import numpy as np
from math import sqrt

async def calculate_number_observation(one_dimensional_array):    
    print('Starting calculate_number_observation...')   
    await asyncio.sleep(0)
    number_of_observation = one_dimensional_array.size
    print("Number Of Observation: {} ".format(number_of_observation))  
    return number_of_observation
   
async def calcuate_arithmetic_mean(one_dimensional_array):    
    print('Starting calcuate_arithmetic_mean...')
    sum_result = 0.0
    await asyncio.sleep(0)
    rows = one_dimensional_array.size  
    for i in range(rows):       
        sum_result += one_dimensional_array[i]    
    arithmetic_mean = sum_result / rows    
    print("Arithmetic Mean: {} ".format(arithmetic_mean))
    print('Finish calcuate_arithmetic_mean...')   
    return arithmetic_mean

async def calculate_median(one_dimensional_array):      
    print('Running calculate_median...')
    await asyncio.sleep(0)
    rows = one_dimensional_array.size  
    one_dimensional_array.sort()    
    half_position = rows // 2
    if not rows % 2:
        median = (one_dimensional_array[half_position - 1] + one_dimensional_array[half_position]) / 2.0
    else:
        median = one_dimensional_array[half_position]        
    print("Median: {} ".format(median))
    return median

async def calculate_sample_standard_deviation(one_dimensional_array):    
    print('Running calculate_sample_standard_deviation...')
    await asyncio.sleep(0)
    sum_result = 0.0
    arithmetic_mean  = await calcuate_arithmetic_mean(one_dimensional_array)
    rows = one_dimensional_array.size       
    for i in range(rows):                   
        sum_result += pow((one_dimensional_array[i] - arithmetic_mean), 2)            
    sample_variance = sum_result / (rows - 1)            
    sample_standard_deviation = sqrt(sample_variance)        
    print("Sample Standard Deviation: {} ".format(sample_standard_deviation))
    return sample_standard_deviation 
    
def main(one_dimensional_array):    
    ioloop = asyncio.get_event_loop()    
    tasks = [ioloop.create_task(calculate_number_observation(one_dimensional_array)),
             ioloop.create_task(calcuate_arithmetic_mean(one_dimensional_array)),
             ioloop.create_task(calculate_median(one_dimensional_array)),
             ioloop.create_task(calculate_sample_standard_deviation(one_dimensional_array))]
    wait_tasks = asyncio.wait(tasks)
    ioloop.run_until_complete(wait_tasks)
    ioloop.close()    
      
if __name__ == '__main__':
    start_time = time.time()  
    one_dimensional_array = np.arange(10000000, dtype=np.float)        
    main(one_dimensional_array)
    end_time = time.time()
    print("Program Runtime: {} seconds".format(round(end_time - start_time, 1)))

    