# -*- coding: utf-8 -*-

import sys
import time

import numpy as np
import pandas as pd
from summary_statistics import SummaryStatistics

def main(data_frame):
    summary_statistics = SummaryStatistics()
    
    number_of_observation = summary_statistics.count(data_frame, "observation")
    print("Number Of Observation: {} ".format(number_of_observation))
    
    arithmetic_mean = summary_statistics.arithmetic_mean(data_frame, "observation")
    print("Arithmetic Mean: {} ".format(arithmetic_mean))
    
    median = summary_statistics.median(data_frame, "observation")
    print("Median: {} ".format(median))
    
#     mode = summary_statistics.mode(data_frame, "observation")
#     print("Mode: {} ".format(mode))
    
    min = summary_statistics.min(data_frame, "observation")
    print("Min: {} ".format(min))
    
    max = summary_statistics.max(data_frame, "observation")
    print("Max: {} ".format(max))    
    
    sample_variance = summary_statistics.sample_variance(data_frame, "observation")
    print("Sample Variance: {} ".format(sample_variance))
    
    sample_standard_deviation = summary_statistics.sample_standard_deviation(data_frame, "observation")
    print("Sample Standard Deviation: {} ".format(sample_standard_deviation))
    
    skewness = summary_statistics.skewness(data_frame, "observation")
    print("Skewness: {} ".format(skewness))
    
    kurtosis = summary_statistics.kurtosis(data_frame, "observation")
    print("Kurtosis: {} ".format(kurtosis))
    
    standard_error_mean = summary_statistics.standard_error_mean(data_frame, "observation")
    print("Standard Error of the Mean: {} ".format(standard_error_mean))
        
if __name__ == '__main__':    
    start_time = time.time()  
    one_dimensional_array = np.arange(100000000, dtype=np.float)    
    data_frame = pd.DataFrame(data = one_dimensional_array, columns = ["observation"])   
    main(data_frame)
    end_time = time.time()
    print("Program Runtime: {} seconds".format(round(end_time - start_time, 1)))
    