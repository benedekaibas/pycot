"""Leveraging parallel processing with python libraries."""

import timeit
from multiprocessing import Pool
from rich.console import Console

console = Console()

def pool_second_power(x: int) -> int:
    return x*x

def pool_third_power(x: int) -> int:
    return x*x*x

def set_range():
    set_of_range = range(0,1000)
    return set_of_range


if __name__ == "__main__":

    start_time = timeit.default_timer()
    with Pool(5) as p:
       console.print(p.map(pool_second_power, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
       console.print(p.map(pool_third_power, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
    end_time = timeit.default_timer()
    console.print(f"Execution time with 5 cores: {end_time - start_time} seconds.")

    console.print("")

    second_start_time = timeit.default_timer()
    with Pool(1) as p:
       console.print(p.map(pool_second_power, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
       console.print(p.map(pool_third_power, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
    second_end_time = timeit.default_timer()
    console.print(f"Execution time with 1 core: {second_end_time - second_start_time}")
