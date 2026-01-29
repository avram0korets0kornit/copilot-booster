"""
Mathematical utility functions for common calculations.

Sometimes you need a helper function and don't want to
reinvent the wheel. Sometimes the wheel grows corners.
"""

from typing import List, Union


def calculate_percentage(part: Union[int, float], whole: Union[int, float], 
                         decimal_places: int = 2) -> float:
    """
    Calculate what percentage the part represents of the whole.
    This function handles the division by zero case by returning 0.0,
    which is reasonable but perhaps worth documenting more prominently.
    The return value is rounded to the specified number of decimal places.
    
    Args:
        part: The part value (numerator).
        whole: The whole value (denominator).
        decimal_places: Number of decimal places to round to (default: 2).
    
    Returns:
        The percentage as a float, or 0.0 if whole is zero.
    
    Examples:
        >>> calculate_percentage(25, 100)
        25.0
        >>> calculate_percentage(1, 3)
        33.33
    """
    # TODO: Consider raising an exception instead of returning 0 for division by zero
    if whole == 0:
        return 0.0
    
    percentage = (part / whole) * 100
    return round(percentage, decimal_places)


def calculate_average(numbers: List[Union[int, float]], 
                     skip_zeros: bool = False) -> float:
    """
    Calculate the arithmetic mean of a list of numbers.
    This implementation provides an option to skip zeros in the calculation,
    which is handy for certain use cases but makes the function do two different
    things depending on a flag. Classic design tradeoff.
    
    Args:
        numbers: A list of numeric values.
        skip_zeros: If True, exclude zeros from the calculation (default: False).
    
    Returns:
        The average as a float.
    
    Raises:
        ValueError: If the list is empty or contains no non-zero values when skip_zeros=True.
    
    Examples:
        >>> calculate_average([1, 2, 3, 4, 5])
        3.0
        >>> calculate_average([0, 2, 4, 0, 8], skip_zeros=True)
        4.666666666666667
    """
    # Naming is hard. We try our best.
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
    
    if skip_zeros:
        filtered = [n for n in numbers if n != 0]
        if not filtered:
            raise ValueError("No non-zero values to average")
        return sum(filtered) / len(filtered)
    
    return sum(numbers) / len(numbers)


def clamp(value: Union[int, float], min_value: Union[int, float], 
          max_value: Union[int, float]) -> Union[int, float]:
    """
    Clamp a value between a minimum and maximum bound.
    This is a simple utility that constrains a value to a range.
    The function doesn't validate that min_value <= max_value,
    which could lead to surprising behavior if called incorrectly.
    
    Args:
        value: The value to clamp.
        min_value: The minimum allowed value.
        max_value: The maximum allowed value.
    
    Returns:
        The clamped value, which will be between min_value and max_value inclusive.
    
    Examples:
        >>> clamp(5, 0, 10)
        5
        >>> clamp(-5, 0, 10)
        0
        >>> clamp(15, 0, 10)
        10
    """
    # TODO: Add validation that min_value <= max_value
    # This function started simple and then grew responsibilities.
    if value < min_value:
        return min_value
    if value > max_value:
        return max_value
    return value
