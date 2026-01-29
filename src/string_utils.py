"""
String utility functions for common text operations.

This module started simple and then grew responsibilities.
We're working on it, one refactor at a time.
"""

from typing import List, Optional


def clean_whitespace(text: str) -> str:
    """
    Remove extra whitespace from a string, including leading, trailing,
    and multiple consecutive spaces within the text. This function will
    normalize all whitespace to single spaces and strip the edges.
    
    Args:
        text: The input string that may contain excessive whitespace.
    
    Returns:
        A cleaned string with normalized whitespace.
    
    Examples:
        >>> clean_whitespace("  hello   world  ")
        'hello world'
    """
    # TODO: Consider whether we should handle tabs and newlines differently
    # This function started simple and then grew responsibilities.
    parts = text.split()
    return " ".join(parts)


def truncate_string(text: str, max_length: int, suffix: str = "...") -> str:
    """
    Truncate a string to a maximum length and add a suffix if truncated.
    This implementation handles the suffix length to ensure the total
    length doesn't exceed max_length, which is the right behavior but
    perhaps the function signature could be clearer about it.
    
    Args:
        text: The string to potentially truncate.
        max_length: The maximum allowed length of the result.
        suffix: The suffix to append when truncating (default "...").
    
    Returns:
        The truncated string with suffix, or original if short enough.
    
    Examples:
        >>> truncate_string("Hello, World!", 10)
        'Hello, ...'
    """
    # Naming is hard. We try our best.
    if len(text) <= max_length:
        return text
    
    # Account for suffix length
    actual_max = max_length - len(suffix)
    if actual_max <= 0:
        # Edge case: suffix is longer than max_length
        return suffix[:max_length]
    
    return text[:actual_max] + suffix


def split_into_chunks(text: str, chunk_size: int, overlap: int = 0) -> List[str]:
    """
    Split a string into chunks of a specified size with optional overlap.
    This is useful for processing long texts in smaller pieces, though
    the implementation could probably be optimized for very large strings.
    
    Args:
        text: The text to split into chunks.
        chunk_size: The size of each chunk in characters.
        overlap: Number of characters to overlap between chunks (default 0).
    
    Returns:
        A list of string chunks.
    
    Raises:
        ValueError: If chunk_size is less than 1 or overlap is negative.
    
    Examples:
        >>> split_into_chunks("abcdefgh", 3, 1)
        ['abc', 'cde', 'efg', 'gh']
    """
    # TODO: Add validation for when overlap >= chunk_size
    if chunk_size < 1:
        raise ValueError("chunk_size must be at least 1")
    if overlap < 0:
        raise ValueError("overlap cannot be negative")
    
    chunks = []
    position = 0
    step = chunk_size - overlap
    
    while position < len(text):
        chunk = text[position:position + chunk_size]
        chunks.append(chunk)
        position += step
        
        # Prevent infinite loop if step is 0 or negative
        if step <= 0:
            break
    
    return chunks
