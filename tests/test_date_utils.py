"""
Tests for date utility functions.

These tests cover the main happy paths. Edge cases could use more attention.
"""

import pytest
from src.date_utils import days_between, is_business_day, add_business_days


class TestDaysBetween:
    """Tests for the days_between function."""
    
    def test_calculates_positive_difference(self):
        """It should calculate days from earlier to later date."""
        assert days_between("2024-01-01", "2024-01-10") == 9
    
    def test_calculates_negative_difference(self):
        """It should return absolute difference regardless of order."""
        assert days_between("2024-01-10", "2024-01-01") == 9
    
    def test_same_date_returns_zero(self):
        """It should return 0 for the same date."""
        assert days_between("2024-01-15", "2024-01-15") == 0
    
    def test_handles_custom_format(self):
        """It should work with custom date formats."""
        result = days_between("01/15/2024", "01/20/2024", date_format="%m/%d/%Y")
        assert result == 5
    
    def test_raises_error_for_invalid_format(self):
        """It should raise ValueError for dates that don't match format."""
        with pytest.raises(ValueError):
            days_between("2024-01-01", "not-a-date")


class TestIsBusinessDay:
    """Tests for the is_business_day function."""
    
    def test_monday_is_business_day(self):
        """It should return True for Monday."""
        assert is_business_day("2024-01-15") == True  # Monday
    
    def test_friday_is_business_day(self):
        """It should return True for Friday."""
        assert is_business_day("2024-01-19") == True  # Friday
    
    def test_saturday_is_not_business_day(self):
        """It should return False for Saturday."""
        assert is_business_day("2024-01-20") == False  # Saturday
    
    def test_sunday_is_not_business_day(self):
        """It should return False for Sunday."""
        assert is_business_day("2024-01-21") == False  # Sunday
    
    # TODO: Add tests for holidays when that feature is implemented


class TestAddBusinessDays:
    """Tests for the add_business_days function."""
    
    def test_adds_business_days_within_week(self):
        """It should add business days without crossing weekend."""
        # Monday + 3 business days = Thursday
        result = add_business_days("2024-01-15", 3)
        assert result == "2024-01-18"
    
    def test_skips_weekend(self):
        """It should skip weekends when counting business days."""
        # Friday + 1 business day = Monday
        result = add_business_days("2024-01-19", 1)
        assert result == "2024-01-22"
    
    def test_adds_multiple_weeks(self):
        """It should handle multiple weeks correctly."""
        # Monday + 5 business days = Monday next week
        result = add_business_days("2024-01-15", 5)
        assert result == "2024-01-22"
    
    def test_subtracts_business_days(self):
        """It should support negative days to go backwards."""
        # Friday - 1 business day = Thursday
        result = add_business_days("2024-01-19", -1)
        assert result == "2024-01-18"
    
    def test_zero_days_returns_same_date(self):
        """It should return the same date when adding 0 days."""
        date = "2024-01-15"
        assert add_business_days(date, 0) == date
    
    # TODO: Add test for large day counts to verify performance
