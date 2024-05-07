# Notes for my research

Vary the pool size: Instead of just comparing pool sizes of 1 and 5, you could run the experiment with a range of pool sizes. This can help you find the optimal pool size for this specific task on your machine. You could use a loop to iterate over a range of pool sizes, and for each size, create a pool and measure the execution time.

Increase the workload: The current tasks (calculating the second and third power of a few numbers) are quite small and might not fully utilize the CPU, especially if you have a powerful machine. You could consider increasing the size of the input list or using a more CPU-intensive task. For example, you could use a larger list of numbers, or a function that performs a more complex calculation.

Repeat the experiment: To account for variability in execution time due to other processes running on your machine, you could repeat the experiment a number of times and calculate the average execution time for each pool size. You could use another loop to repeat the experiment, and a list to store the execution times for each repetition. Then, you could calculate the average execution time by summing the times and dividing by the number of repetitions.

Use a more complex function: The functions pool_second_power and pool_third_power are quite simple. Using a more complex function might give you a better idea of the benefits of parallel processing. For example, you could use a function that performs a complex mathematical operation, or a function that processes a large amount of data.

Measure memory usage: In addition to execution time, you could also measure the memory usage of your program. This could give you a better idea of the resources required by your program, and help you optimize it further. You could use a library like memory_profiler to measure memory usage.

Compare with sequential execution: To get a better idea of the benefits of parallel processing, you could compare the execution time with the time it takes to execute the same tasks sequentially (without using a pool). This could give you a better idea of the speedup achieved by parallel processing.
