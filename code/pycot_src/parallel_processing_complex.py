"""Leveraging parallel processing in python in a more complex way."""

import timeit
from multiprocessing import Pool
from rich.console import Console
from typing import List

# TODO: iterate through the possible pool sizes - DONE
# TODO: create a range that we can perform a doubling experiment to its every values
# TODO: for each pool size return the result of the iteration with the doubling function


console = Console()

class LPPComplex:
    def __init__(self) -> None:
        pass
    
    def cpu_cores(self):
        """Returning all the cores that laptops could have."""
        return [2,3,4,5,6,7,8]
    
    def experiment(self):
        """Do experiment for every single core and return the experiment"""
        cores = self.cpu_cores()

        for item in cores:
            console.print(f"{item} in for {cores} core: {item ** item}")





if __name__ == "__main__":
    lpp_complex =  LPPComplex()
    console.print(lpp_complex.experiment())
