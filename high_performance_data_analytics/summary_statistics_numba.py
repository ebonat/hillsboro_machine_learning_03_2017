
# Numba
# http://numba.pydata.org/

import time

from numba import jit
import numpy as np
from math import sqrt

# @jit
def calculate_number_observation(one_dimensional_array):    
    number_observation = one_dimensional_array.size
    return number_observation
    
# @jit
def calcuate_arithmetic_mean(one_dimensional_array):    
    sum_result = 0.0
    rows = one_dimensional_array.size    
    for i in range(rows):       
        sum_result += one_dimensional_array[i]    
    arithmetic_mean = sum_result / rows
    return arithmetic_mean

# @jit
def calculate_median(one_dimensional_array):      
    rows = one_dimensional_array.size  
    one_dimensional_array.sort()    
    half_position = rows // 2
    if not rows % 2:
        median = (one_dimensional_array[half_position - 1] + one_dimensional_array[half_position]) / 2.0
    else:
        median = one_dimensional_array[half_position]        
    return median

# @jit
def calculate_sample_standard_deviation(one_dimensional_array, arithmetic_mean):    
    sum_result = 0.0
    rows = one_dimensional_array.size    
    for i in range(rows):                   
        sum_result += pow((one_dimensional_array[i] - arithmetic_mean), 2)            
    sample_variance = sum_result / (rows - 1)            
    sample_standard_deviation = sqrt(sample_variance)        
    return sample_standard_deviation 
    
def main(one_dimensional_array):
    
    number_of_observation = calculate_number_observation(one_dimensional_array)
    print("Number Of Observation: {} ".format(number_of_observation))
    
    arithmetic_mean = calcuate_arithmetic_mean(one_dimensional_array)
    print("Arithmetic Mean: {} ".format(arithmetic_mean))
      
    median = calculate_median(one_dimensional_array)
    print("Median: {} ".format(median))
    
    sample_standard_deviation = calculate_sample_standard_deviation(one_dimensional_array, arithmetic_mean)
    print("Sample Standard Deviation: {} ".format(sample_standard_deviation))
      
if __name__ == '__main__':
    start_time = time.time()  
    one_dimensional_array = np.arange(100000000, dtype=np.float)        
    main(one_dimensional_array)
    end_time = time.time()
    print("Program Runtime: {} seconds".format(round(end_time - start_time, 1)))

    