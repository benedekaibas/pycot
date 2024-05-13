"""Leveraging parallel processing in python in a more complex way."""

import timeit
from multiprocessing import Pool
from rich.console import Console
from typing import List


console = Console()

class LPPComplex:
    def __init__(self) -> None:
        pass

    def pool_size(self) -> List[int]:
        """Iterating through the pool sizes."""
        #range of possible pool sizes
        pool = [1,2,3,4,5]
        for i in pool:
            return Pool(i)

    def pool_second_power(self, number: int) -> int:
        """Raising the parameter to its second power."""
        return number ** number

    

if __name__ == "__main__":
    lpp_complex = LPPComplex()
    console.print(lpp_complex.pool_size())
