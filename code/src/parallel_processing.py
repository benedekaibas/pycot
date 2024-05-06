"""Leveraging parallel processing with python libraries."""

from multiprocessing import Pool
from rich.console import Console

console = Console()

def pool(x: int) -> int:
    return x*x

if __name__ == "__main__":
    with Pool(5) as p:
       console.print(p.map(pool, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
