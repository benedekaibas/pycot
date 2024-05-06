"""Optimizing function calls."""

import timeit
from typing import List

myList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] * 1000
oddList = []
evenList = []

start_time = timeit.default_timer()

for i in myList:
    if i % 2 != 0:
        oddList.append(i)
    else:
        evenList.append(i)

end_time = timeit.default_timer()

print(f"Execution time: {end_time - start_time} seconds")

class OPTFunction:
    """Class for doing research in optimizing function calls."""

    def __init__(self) -> None:
        """Init function for the class."""
        pass

    def optimized_function(oddList: List, evenList: List, start_time: float, end_time: float) -> List:
        myList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] * 1000

        start_time = timeit.default_timer()

        for i in myList:
            if i % 2 != 0:
                oddList.append(i)
            else:
                evenList.append(i)

        end_time = timeit.default_timer()
