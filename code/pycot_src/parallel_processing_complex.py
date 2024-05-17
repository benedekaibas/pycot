"""Leveraging parallel processing in python in a more complex way."""

import timeit
from multiprocessing import Pool
from rich.console import Console
from typing import List

# iterate through the possible pool sizes - DONE
# create a range that we can perform a doubling experiment to its every values - DONE
# for each pool size return the result of the iteration with the doubling function - DONE
# TODO: Instead of using for loop use some of the searching methods, e.g: binary search, recursive search, etc.

console = Console()

class LPPComplex:
    def __init__(self) -> None:
        pass
    
    def set_range(self):
        return list(range(1, 1001))

    def cpu_cores(self):
        """Returning all the cores that laptops could have."""
        return [2,3,4,5,6,7,8] # possible cores that a laptop has
    
    def pool_second_power(self, number: int) -> int:
        return number ** number
    
    def experiment_for_loop(self) -> list:
        """Do experiment for every single core and return the experiment"""
        results = []
        for core in self.cpu_cores():
            start_time = timeit.default_timer()
            with Pool(core) as p:
                result = p.map(self.pool_second_power, self.set_range())
                results.append((core, result))
            end_time = timeit.default_timer()
            console.print(f"Execution time with {core} cores: {end_time - start_time} seconds.")
        return results
    
    def experiment_binary_search(self, lst = list, item = int, left = 0, right = None) -> list: 
        """Doing the experiment with binary search, so we can get a better execution time."""
        if right is None:
            right = len(lst)
        
        if right - left <= 1:
            return right > left and lst(left) == item
        
        median = (right + left) // 2
        if item < lst[median]:
            return self.experiment_binary_search(lst, item, left, median)
        else:
            return self.experiment_binary_search(lst, item, median, right)



if __name__ == "__main__":
    lpp_complex =  LPPComplex()
    console.print(lpp_complex.experiment_for_loop())
    console.print(lpp_complex.experiment_binary_search())
