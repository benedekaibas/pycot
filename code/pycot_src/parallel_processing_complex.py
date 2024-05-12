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
        #second_power = pool_second_power() # we might use it in a different way
        pool = [1,2,3,4,5]
        for i in pool:
            return Pool(i)


if __name__ == "__main__":
    lpp_complex = LPPComplex()
    console.print(lpp_complex.pool_size())
