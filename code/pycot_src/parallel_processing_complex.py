"""Leveraging parallel processing in python in a more complex way."""

import timeit
from multiprocessing import Pool
from rich.console import Console
from typing import List

# TODO: iterate through the possible pool sizes
# TODO: create a range that we can perform a doubling experiment to its every values
# TODO: for each pool size return the result of the iteration with the doubling function


console = Console()

class LPPComplex:
    def __init__(self) -> None:
        pass
    
    def pool_size(self):
        return list(range(1000))

if __name__ == "__main__":
    lpp_complex =  LPPComplex()
    console.print(lpp_complex.pool_size())