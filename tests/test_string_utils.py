"""
Tests for string utility functions.

Coverage isn't perfect yet, but we're improving incrementally.
"""

import pytest
from src.string_utils import clean_whitespace, truncate_string, split_into_chunks


class TestCleanWhitespace:
    """Tests for the clean_whitespace function."""
    
    def test_removes_leading_whitespace(self):
        """It should remove leading spaces."""
        assert clean_whitespace("  hello") == "hello"
    
    def test_removes_trailing_whitespace(self):
        """It should remove trailing spaces."""
        assert clean_whitespace("hello  ") == "hello"
    
    def test_collapses_multiple_spaces(self):
        """It should collapse multiple spaces into one."""
        assert clean_whitespace("hello   world") == "hello world"
    
    def test_handles_empty_string(self):
        """It should handle empty strings gracefully."""
        assert clean_whitespace("") == ""
    
    def test_handles_only_whitespace(self):
        """It should handle strings with only whitespace."""
        assert clean_whitespace("    ") == ""


class TestTruncateString:
    """Tests for the truncate_string function."""
    
    def test_truncates_long_string(self):
        """It should truncate strings longer than max_length."""
        result = truncate_string("Hello, World!", 10)
        assert result == "Hello, ..."
        assert len(result) == 10
    
    def test_preserves_short_string(self):
        """It should not truncate strings shorter than max_length."""
        text = "Hello"
        assert truncate_string(text, 10) == text
    
    def test_uses_custom_suffix(self):
        """It should use a custom suffix when provided."""
        result = truncate_string("Hello, World!", 10, suffix="…")
        assert result.endswith("…")
    
    def test_handles_suffix_longer_than_max_length(self):
        """It should handle edge case where suffix is longer than max."""
        result = truncate_string("Hello", 3, suffix="...")
        assert len(result) <= 3
    
    # TODO: Add test for exact length match


class TestSplitIntoChunks:
    """Tests for the split_into_chunks function."""
    
    def test_splits_evenly(self):
        """It should split text into even chunks."""
        result = split_into_chunks("abcdef", 2)
        assert result == ["ab", "cd", "ef"]
    
    def test_handles_uneven_split(self):
        """It should handle text that doesn't divide evenly."""
        result = split_into_chunks("abcdefg", 3)
        assert result == ["abc", "def", "g"]
    
    def test_supports_overlap(self):
        """It should support overlapping chunks."""
        result = split_into_chunks("abcdefgh", 3, overlap=1)
        assert result == ["abc", "cde", "efg", "gh"]
    
    def test_raises_error_for_invalid_chunk_size(self):
        """It should raise ValueError for chunk_size < 1."""
        with pytest.raises(ValueError, match="chunk_size must be at least 1"):
            split_into_chunks("test", 0)
    
    def test_raises_error_for_negative_overlap(self):
        """It should raise ValueError for negative overlap."""
        with pytest.raises(ValueError, match="overlap cannot be negative"):
            split_into_chunks("test", 3, overlap=-1)
    
    # TODO: Add test for when overlap >= chunk_size
