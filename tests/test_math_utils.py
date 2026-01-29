"""
Tests for mathematical utility functions.

Testing math is straightforward. Testing edge cases... that's the real work.
"""

import pytest
from src.math_utils import calculate_percentage, calculate_average, clamp


class TestCalculatePercentage:
    """Tests for the calculate_percentage function."""
    
    def test_calculates_simple_percentage(self):
        """It should calculate basic percentages correctly."""
        assert calculate_percentage(25, 100) == 25.0
    
    def test_calculates_fractional_percentage(self):
        """It should handle fractional results."""
        assert calculate_percentage(1, 3) == 33.33
    
    def test_handles_zero_whole(self):
        """It should return 0.0 when whole is zero."""
        assert calculate_percentage(5, 0) == 0.0
    
    def test_respects_decimal_places(self):
        """It should round to specified decimal places."""
        result = calculate_percentage(1, 3, decimal_places=4)
        assert result == 33.3333
    
    def test_handles_larger_part_than_whole(self):
        """It should handle percentages over 100."""
        assert calculate_percentage(150, 100) == 150.0
    
    # TODO: Add test for negative numbers


class TestCalculateAverage:
    """Tests for the calculate_average function."""
    
    def test_calculates_simple_average(self):
        """It should calculate the mean of a list."""
        assert calculate_average([1, 2, 3, 4, 5]) == 3.0
    
    def test_handles_single_value(self):
        """It should work with a single value."""
        assert calculate_average([42]) == 42.0
    
    def test_handles_floats(self):
        """It should work with floating point numbers."""
        assert calculate_average([1.5, 2.5, 3.0]) == pytest.approx(2.333, rel=0.01)
    
    def test_raises_error_for_empty_list(self):
        """It should raise ValueError for empty list."""
        with pytest.raises(ValueError, match="Cannot calculate average of empty list"):
            calculate_average([])
    
    def test_skip_zeros_excludes_zeros(self):
        """It should exclude zeros when skip_zeros is True."""
        result = calculate_average([0, 2, 4, 0, 8], skip_zeros=True)
        # Average of [2, 4, 8] = 14/3 ≈ 4.667
        assert result == pytest.approx(4.667, rel=0.01)
    
    def test_skip_zeros_raises_error_if_all_zeros(self):
        """It should raise error when all values are zero and skip_zeros=True."""
        with pytest.raises(ValueError, match="No non-zero values to average"):
            calculate_average([0, 0, 0], skip_zeros=True)


class TestClamp:
    """Tests for the clamp function."""
    
    def test_returns_value_within_range(self):
        """It should return the value if already within range."""
        assert clamp(5, 0, 10) == 5
    
    def test_clamps_to_minimum(self):
        """It should clamp to minimum if value is too low."""
        assert clamp(-5, 0, 10) == 0
    
    def test_clamps_to_maximum(self):
        """It should clamp to maximum if value is too high."""
        assert clamp(15, 0, 10) == 10
    
    def test_handles_floats(self):
        """It should work with floating point numbers."""
        assert clamp(3.7, 0.0, 5.0) == 3.7
    
    def test_handles_equal_bounds(self):
        """It should handle the case where min equals max."""
        assert clamp(5, 3, 3) == 3
    
    # TODO: Add test for when min_value > max_value (current bug)
