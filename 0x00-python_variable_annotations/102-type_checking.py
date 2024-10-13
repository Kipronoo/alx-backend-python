#!/usr/bin/env python3
'''
Use mypy to validate the following piece of code
'''
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    '''Type Checking'''
    zoomed_in = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)  # Use tuple instead of list

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)  # Pass an integer instead of a float
