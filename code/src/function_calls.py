"""Optimizing function calls."""

import timeit
from typing import List
from rich.console import Console

console = Console()

myList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] * 10000
oddList = []
evenList = []

start_time = timeit.default_timer()

for i in myList:
    if i % 2 != 0:
        oddList.append(i)
    else:
        evenList.append(i)

end_time = timeit.default_timer()

console.print("Directly scripted code method")
console.print("")
console.print(f"Execution time: {end_time - start_time} seconds")

class OPTFunction:
    """Class for doing research in optimizing function calls."""

    def optimized_function(self, oddList: List, evenList: List) -> str:
        myList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] * 10000

        start_time = timeit.default_timer()

        for i in myList:
            if i % 2 != 0:
                oddList.append(i)
            else:
                evenList.append(i)

        end_time = timeit.default_timer()

        return f"Execution time: {end_time - start_time} seconds"

if __name__ == "__main__":
    opt_function = OPTFunction()
    oddList = []
    evenList = []
    console.print("")
    console.print("Function method")
    console.print("")
    console.print(opt_function.optimized_function(oddList, evenList))



