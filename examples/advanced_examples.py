"""
Advanced Examples - Copilot Simulator

This file demonstrates advanced features of the Copilot simulator,
showing how it handles complex scenarios and provides detailed insights.
"""

import sys
import os

# Add parent directory to path to import copilot_simulator
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from copilot_simulator import CopilotSimulator, CodeContext, ContextGatherer


def example_verbose_mode():
    """Example: Running with verbose mode to see all phases"""
    print("\n" + "=" * 70)
    print("EXAMPLE: Verbose Mode - See All Internal Phases")
    print("=" * 70)
    
    code = """import requests
from typing import Optional

def fetch_user_data(user_id: int) -> Optional[dict]:
    # Fetch user data from API
"""
    
    simulator = CopilotSimulator()
    
    print("\nRunning simulation with verbose=True to see internal phases...")
    print("\n")
    
    suggestions = simulator.get_suggestions(
        file_content=code,
        cursor_position=(5, 0),
        file_path="api_client.py",
        verbose=True  # This shows all internal phases
    )
    
    print("\n📊 Analysis:")
    print(f"  - Total suggestions generated: {len(suggestions)}")
    print(f"  - Highest confidence: {suggestions[0].confidence:.2%}" if suggestions else "  - No suggestions")


def example_context_analysis():
    """Example: Analyzing the context gathering phase"""
    print("\n" + "=" * 70)
    print("EXAMPLE: Context Gathering Analysis")
    print("=" * 70)
    
    code = """#!/usr/bin/env python3
# Module for processing customer data.

import json
import logging
from datetime import datetime
from typing import List, Dict, Any

# Configure logging
logger = logging.getLogger(__name__)

class CustomerProcessor:
    # Processes customer data and generates reports.
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.customers = []
    
    def add_customer(self, customer_data: Dict[str, Any]) -> None:
        # Validate customer data before adding
"""
    
    gatherer = ContextGatherer()
    context = gatherer.gather_context(code, cursor_position=(23, 0), file_path="customer_processor.py")
    
    print("\n📋 Gathered Context Details:")
    print(f"  File: {context.file_path}")
    print(f"  Language: {context.language}")
    print(f"  Cursor Position: Line {context.cursor_line}, Column {context.cursor_column}")
    print(f"\n  Total lines before cursor: {len(context.lines_before_cursor)}")
    print(f"  Total lines after cursor: {len(context.lines_after_cursor)}")
    
    print(f"\n  📦 Imports found ({len(context.imports)}):")
    for imp in context.imports:
        print(f"    - {imp}")
    
    print(f"\n  💬 Comments found ({len(context.comments)}):")
    for comment in context.comments[:5]:  # Show first 5
        print(f"    - {comment.strip()}")
    
    print(f"\n  📝 Last 3 lines before cursor:")
    for i, line in enumerate(context.lines_before_cursor[-3:], 1):
        print(f"    {i}. {line}")
    
    # Now get suggestions
    simulator = CopilotSimulator()
    suggestions = simulator.get_suggestions(
        file_content=code,
        cursor_position=(23, 0),
        file_path="customer_processor.py",
        verbose=False
    )
    
    print(f"\n  💡 Generated {len(suggestions)} suggestions")
    if suggestions:
        print(f"\n  Top suggestion (confidence: {suggestions[0].confidence:.2%}):")
        print(f"    {suggestions[0].text}")


def example_multiple_scenarios():
    """Example: Comparing suggestions across different scenarios"""
    print("\n" + "=" * 70)
    print("EXAMPLE: Comparing Suggestions Across Scenarios")
    print("=" * 70)
    
    scenarios = [
        {
            "name": "After Function Definition",
            "code": "def process_payment(amount, currency):",
            "cursor": (1, 0),
            "file": "payment.py"
        },
        {
            "name": "After Class Definition",
            "code": "class PaymentGateway:",
            "cursor": (1, 0),
            "file": "gateway.py"
        },
        {
            "name": "After Loop Comment",
            "code": "# Iterate through all transactions",
            "cursor": (1, 0),
            "file": "transactions.py"
        },
        {
            "name": "After Validation Comment",
            "code": "# Check if the user has sufficient balance",
            "cursor": (1, 0),
            "file": "balance.py"
        }
    ]
    
    simulator = CopilotSimulator()
    
    for scenario in scenarios:
        print(f"\n{'─' * 70}")
        print(f"📍 Scenario: {scenario['name']}")
        print(f"   Code: {scenario['code']}")
        
        suggestions = simulator.get_suggestions(
            file_content=scenario['code'],
            cursor_position=scenario['cursor'],
            file_path=scenario['file'],
            verbose=False
        )
        
        print(f"\n   Suggestions ({len(suggestions)} total):")
        for i, sug in enumerate(suggestions[:2], 1):  # Show top 2
            print(f"\n   {i}. Confidence: {sug.confidence:.2%}")
            print(f"      Reasoning: {sug.reasoning}")
            print(f"      Code: {sug.text[:60]}{'...' if len(sug.text) > 60 else ''}")


def example_confidence_scores():
    """Example: Understanding confidence scores"""
    print("\n" + "=" * 70)
    print("EXAMPLE: Understanding Confidence Scores")
    print("=" * 70)
    
    print("\nConfidence scores indicate how certain Copilot is about a suggestion:")
    print("  - 0.90+ : Very high confidence (common, well-established patterns)")
    print("  - 0.70-0.89: High confidence (likely correct)")
    print("  - 0.50-0.69: Medium confidence (reasonable suggestion)")
    print("  - 0.40-0.49: Low confidence (speculative)")
    print("  - Below 0.40: Filtered out (too uncertain)")
    
    test_cases = [
        ("class Database:", "Class definitions almost always start with __init__"),
        ("def calculate(x, y):", "Functions often start with docstrings"),
        ("# Loop through items", "Comment suggests iteration, but implementation varies"),
    ]
    
    simulator = CopilotSimulator()
    
    for code, explanation in test_cases:
        print(f"\n{'─' * 70}")
        print(f"Code: {code}")
        print(f"Why: {explanation}")
        
        suggestions = simulator.get_suggestions(
            file_content=code,
            cursor_position=(1, 0),
            file_path="test.py",
            verbose=False
        )
        
        if suggestions:
            print(f"\nTop suggestion confidence: {suggestions[0].confidence:.2%}")
            print(f"Interpretation: ", end="")
            conf = suggestions[0].confidence
            if conf >= 0.90:
                print("Very confident - this is a well-established pattern")
            elif conf >= 0.70:
                print("Confident - this is a likely correct suggestion")
            elif conf >= 0.50:
                print("Moderate - this is a reasonable possibility")
            else:
                print("Low - this is more speculative")


def main():
    """Run all advanced examples"""
    print("\n" + "=" * 70)
    print("COPILOT SIMULATOR - ADVANCED EXAMPLES")
    print("=" * 70)
    print("\nThese examples demonstrate advanced features and provide")
    print("deeper insights into how Copilot works internally.\n")
    
    example_verbose_mode()
    example_context_analysis()
    example_multiple_scenarios()
    example_confidence_scores()
    
    print("\n" + "=" * 70)
    print("ALL ADVANCED EXAMPLES COMPLETE")
    print("=" * 70)
    print("\nKey Insights:")
    print("1. Context gathering is comprehensive (imports, comments, code structure)")
    print("2. Prompt generation structures context optimally for the ML model")
    print("3. Confidence scores reflect pattern frequency and certainty")
    print("4. Different code patterns trigger different suggestion strategies")
    print("5. Verbose mode helps understand the internal decision-making process")
    print("\n")


if __name__ == "__main__":
    main()
