import time
from convert_to_snake_case_iteration import convert_to_snake_case_iteration
from convert_to_snake_case_list import convert_to_snake_case_list

def main():
    test_string = 'aLongAndComplexString'
    
    start_time = time.time()
    result1 = convert_to_snake_case_iteration(test_string)
    end_time = time.time()
    time1 = end_time - start_time
    
    start_time = time.time()
    result2 = convert_to_snake_case_list(test_string)
    end_time = time.time()
    time2 = end_time - start_time
    
    print(f"Iteration Approach Result: {result1}")
    print(f"Iteration Approach Execution Time: {time1:.10f} seconds")
    
    print(f"List Approach Result: {result2}")
    print(f"List Approach Execution Time: {time2:.10f} seconds")
    
    if time1 > time2:
        speedup = time1 / time2
        print(f"List Approach is {speedup:.2f} times faster than Iteration Approach")
    else:
        speedup = time2 / time1
        print(f"Iteration Approach is {speedup:.2f} times faster than List Approach")

if __name__ == '__main__':
    main()
