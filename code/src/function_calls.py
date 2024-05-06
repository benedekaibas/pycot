"""Optimizing function calls."""


myList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] * 1000
oddList = []
evenList = []

for i in myList:
    if i % 2 != 0:
        oddList.append(i)
    else:
        evenList.append(i)


class OPTFunction:
    """Class for doing research in optimizing function calls."""

    def __init__(self) -> None:
        """Init function for the class."""
        pass
