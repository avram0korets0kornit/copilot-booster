"""
Basic Examples - Copilot Simulator

This file demonstrates basic usage of the Copilot simulator
with simple, common coding scenarios.
"""

import sys
import os

# Add parent directory to path to import copilot_simulator
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from copilot_simulator import CopilotSimulator


def example_function_docstring():
    """Example: Suggesting docstring after function definition"""
    print("\n" + "=" * 70)
    print("EXAMPLE: Function Docstring Suggestion")
    print("=" * 70)
    
    code = """def calculate_average(numbers):"""
    
    simulator = CopilotSimulator()
    suggestions = simulator.get_suggestions(
        file_content=code,
        cursor_position=(1, 0),
        file_path="math_utils.py",
        verbose=False
    )
    
    print(f"\nCode context:\n{code}")
    print(f"\nCursor position: Line 1, Column 0")
    print(f"\nTop suggestions:")
    for i, sug in enumerate(suggestions[:3], 1):
        print(f"\n{i}. Confidence: {sug.confidence:.2%}")
        print(f"   Reasoning: {sug.reasoning}")
        print(f"   Suggestion:\n{sug.text}")


def example_class_initialization():
    """Example: Suggesting __init__ after class definition"""
    print("\n" + "=" * 70)
    print("EXAMPLE: Class Initialization Suggestion")
    print("=" * 70)
    
    code = """class UserAccount:"""
    
    simulator = CopilotSimulator()
    suggestions = simulator.get_suggestions(
        file_content=code,
        cursor_position=(1, 0),
        file_path="models.py",
        verbose=False
    )
    
    print(f"\nCode context:\n{code}")
    print(f"\nCursor position: Line 1, Column 0")
    print(f"\nTop suggestions:")
    for i, sug in enumerate(suggestions[:3], 1):
        print(f"\n{i}. Confidence: {sug.confidence:.2%}")
        print(f"   Reasoning: {sug.reasoning}")
        print(f"   Suggestion:\n{sug.text}")


def example_comment_to_code():
    """Example: Suggesting code based on comment"""
    print("\n" + "=" * 70)
    print("EXAMPLE: Comment to Code Suggestion")
    print("=" * 70)
    
    code = """# Loop through all users and validate their email addresses"""
    
    simulator = CopilotSimulator()
    suggestions = simulator.get_suggestions(
        file_content=code,
        cursor_position=(1, 0),
        file_path="validation.py",
        verbose=False
    )
    
    print(f"\nCode context:\n{code}")
    print(f"\nCursor position: Line 1, Column 0")
    print(f"\nTop suggestions:")
    for i, sug in enumerate(suggestions[:3], 1):
        print(f"\n{i}. Confidence: {sug.confidence:.2%}")
        print(f"   Reasoning: {sug.reasoning}")
        print(f"   Suggestion:\n{sug.text}")


def example_with_context():
    """Example: Suggestions with richer context"""
    print("\n" + "=" * 70)
    print("EXAMPLE: Suggestions with Rich Context")
    print("=" * 70)
    
    code = """import json
import os
from typing import List, Dict

class DataProcessor:
    def __init__(self, config_path: str):
        self.config_path = config_path
        self.data = []
    
    def load_data(self, file_path: str):
        # Load JSON data from file
"""
    
    simulator = CopilotSimulator()
    suggestions = simulator.get_suggestions(
        file_content=code,
        cursor_position=(11, 0),
        file_path="processor.py",
        verbose=False
    )
    
    print(f"\nCode context (showing last 5 lines):")
    print('\n'.join(code.split('\n')[-5:]))
    print(f"\nCursor position: Line 11, Column 0")
    print(f"\nTop suggestions:")
    for i, sug in enumerate(suggestions[:3], 1):
        print(f"\n{i}. Confidence: {sug.confidence:.2%}")
        print(f"   Reasoning: {sug.reasoning}")
        print(f"   Suggestion:\n{sug.text}")


def main():
    """Run all basic examples"""
    print("\n" + "=" * 70)
    print("COPILOT SIMULATOR - BASIC EXAMPLES")
    print("=" * 70)
    print("\nThese examples demonstrate how Copilot generates suggestions")
    print("in common coding scenarios.\n")
    
    example_function_docstring()
    example_class_initialization()
    example_comment_to_code()
    example_with_context()
    
    print("\n" + "=" * 70)
    print("ALL EXAMPLES COMPLETE")
    print("=" * 70)
    print("\nKey Takeaways:")
    print("1. Copilot analyzes the code context around your cursor")
    print("2. It recognizes common patterns (functions, classes, comments)")
    print("3. It generates multiple suggestions with confidence scores")
    print("4. Higher confidence suggestions are ranked first")
    print("5. The suggestions are based on learned patterns from training data")
    print("\n")


if __name__ == "__main__":
    main()
