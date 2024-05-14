"""Leveraging parallel processing in python in a more complex way."""

import timeit
from multiprocessing import Pool
from rich.console import Console
from typing import List

# iterate through the possible pool sizes - DONE
# create a range that we can perform a doubling experiment to its every values - DONE
# for each pool size return the result of the iteration with the doubling function - DONE


console = Console()

class LPPComplex:
    def __init__(self) -> None:
        pass
    
    def set_range(self):
        return range(1, 1001)

    def cpu_cores(self):
        """Returning all the cores that laptops could have."""
        return [2,3,4,5,6,7,8]
    
    def pool_second_power(self, number: int) -> int:
        return number ** number
    
    def experiment(self):
        """Do experiment for every single core and return the experiment"""
        cores = self.cpu_cores()
        pool_second_power = self.pool_second_power(10)
        set_range = self.set_range()


        results = []
        for core in cores:
            start_time = timeit.default_timer()
            with Pool(core) as p:
                result = p.map(pool_second_power, set_range)
                results.append((core, result))
            end_time = timeit.default_timer()
            console.print(f"Execution time with {core} cores: {end_time - start_time} seconds.")
        return results
            



if __name__ == "__main__":
    lpp_complex =  LPPComplex()
    console.print(lpp_complex.experiment())
