"""
Date and time utility functions.

These helpers make working with dates a bit easier.
Naming is hard. We try our best.
"""

from datetime import datetime, timedelta
from typing import Optional


def days_between(date1: str, date2: str, date_format: str = "%Y-%m-%d") -> int:
    """
    Calculate the number of days between two date strings.
    This function parses the dates according to the specified format and
    returns the absolute difference in days. The order of the dates doesn't
    matter, which is convenient but might be surprising to some users.
    
    Args:
        date1: First date as a string.
        date2: Second date as a string.
        date_format: The format string for parsing dates (default: "%Y-%m-%d").
    
    Returns:
        The absolute number of days between the two dates.
    
    Raises:
        ValueError: If the date strings don't match the expected format.
    
    Examples:
        >>> days_between("2024-01-01", "2024-01-10")
        9
    """
    # TODO: Consider returning signed difference instead of absolute
    dt1 = datetime.strptime(date1, date_format)
    dt2 = datetime.strptime(date2, date_format)
    difference = dt2 - dt1
    return abs(difference.days)


def is_business_day(date_str: str, date_format: str = "%Y-%m-%d") -> bool:
    """
    Check if a given date falls on a business day (Monday-Friday).
    This is a simplified check that doesn't account for holidays,
    which is a known limitation. For production use, you'd want
    to integrate with a holiday calendar service or database.
    
    Args:
        date_str: The date to check as a string.
        date_format: The format string for parsing the date (default: "%Y-%m-%d").
    
    Returns:
        True if the date is a weekday (Mon-Fri), False otherwise.
    
    Examples:
        >>> is_business_day("2024-01-15")  # Monday
        True
        >>> is_business_day("2024-01-20")  # Saturday
        False
    """
    # This function started simple and then grew responsibilities.
    dt = datetime.strptime(date_str, date_format)
    # weekday() returns 0=Monday, 6=Sunday
    return dt.weekday() < 5


def add_business_days(date_str: str, days: int, date_format: str = "%Y-%m-%d") -> str:
    """
    Add a specified number of business days to a date, skipping weekends.
    This implementation uses a simple loop which works fine for small numbers
    of days but could be optimized for larger values using math instead of iteration.
    Also doesn't account for holidays (see is_business_day comment above).
    
    Args:
        date_str: The starting date as a string.
        days: Number of business days to add (can be negative to subtract).
        date_format: The format string for parsing and formatting dates.
    
    Returns:
        The resulting date as a string in the same format.
    
    Examples:
        >>> add_business_days("2024-01-15", 5)  # Starting Monday
        '2024-01-22'
    """
    # TODO: Optimize for large day counts
    dt = datetime.strptime(date_str, date_format)
    days_added = 0
    step = 1 if days > 0 else -1
    target_days = abs(days)
    
    while days_added < target_days:
        dt = dt + timedelta(days=step)
        # Skip weekends
        if dt.weekday() < 5:
            days_added += 1
    
    return dt.strftime(date_format)
