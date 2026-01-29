# Quick Start Guide - Copilot Booster

This guide will help you get started with the Copilot Simulator in under 5 minutes.

## What is Copilot Booster?

Copilot Booster is an educational simulation that demonstrates how GitHub Copilot works internally. It's designed to help developers understand:
- How AI code assistants gather context from your code
- How they generate suggestions
- Why certain suggestions are ranked higher than others
- How security and quality checks work

## Installation

No installation required! The simulator is pure Python with no external dependencies.

```bash
# Clone the repository (replace with your actual repository URL)
git clone https://github.com/YOUR_USERNAME/copilot-booster.git
cd copilot-booster
```

## Running Your First Simulation

### Option 1: Run the Main Demo

```bash
python copilot_simulator.py
```

This will show you three examples demonstrating how Copilot generates suggestions after:
1. Function definitions
2. Class definitions
3. Comments describing actions

### Option 2: Run Basic Examples

```bash
python examples/basic_examples.py
```

This demonstrates common coding scenarios with clear, simple outputs.

### Option 3: Run Advanced Examples

```bash
python examples/advanced_examples.py
```

This provides deeper insights with:
- Verbose mode showing all internal phases
- Context gathering analysis
- Comparison across multiple scenarios
- Confidence score explanations

## Using in Your Own Code

Create a new Python file:

```python
from copilot_simulator import CopilotSimulator

# Create a simulator
simulator = CopilotSimulator()

# Your code where you want suggestions
code = """
def calculate_total(items):
"""

# Get suggestions at cursor position
suggestions = simulator.get_suggestions(
    file_content=code,
    cursor_position=(2, 0),  # Line 2, Column 0
    file_path="example.py",
    verbose=True  # Set to False for less output
)

# Display suggestions
for i, suggestion in enumerate(suggestions, 1):
    print(f"\n{i}. Suggestion (Confidence: {suggestion.confidence:.2%})")
    print(f"   {suggestion.text}")
    print(f"   Reason: {suggestion.reasoning}")
```

## Understanding the Output

When you run with `verbose=True`, you'll see four phases:

### Phase 1: Context Gathering
```
[Phase 1] Context Gathering
------------------------------------------------------------
Gathered context: CodeContext(file=example.py, language=py, line=2)
  - Lines before cursor: 2
  - Imports found: 0
  - Comments found: 0
```

This shows what information Copilot collected from your code.

### Phase 2: Prompt Generation
```
[Phase 2] Prompt Generation
------------------------------------------------------------
Generated prompt for language model:
# File: example.py
# Language: py

def calculate_total(items):
<|CURSOR|>
```

This is the formatted prompt sent to the ML model.

### Phase 3: Suggestion Generation
```
[Phase 3] Suggestion Generation
------------------------------------------------------------
Generated 2 suggestions:
  1. Suggestion(confidence=0.85): """Calculate total..."""
  2. Suggestion(confidence=0.70): pass
```

This shows all generated suggestions with confidence scores.

### Phase 4: Ranking & Filtering
```
[Phase 4] Ranking & Filtering
------------------------------------------------------------
After filtering: 2 suggestions remain
Final ranked suggestions:
  1. Suggestion(confidence=0.85): """Calculate total..."""
```

This shows the final filtered and ranked suggestions.

## Key Concepts

### Confidence Scores

- **0.90+**: Very high confidence (well-established patterns)
- **0.70-0.89**: High confidence (likely correct)
- **0.50-0.69**: Medium confidence (reasonable)
- **0.40-0.49**: Low confidence (speculative)
- **Below 0.40**: Filtered out

### Context Matters

Copilot considers:
- Code before the cursor
- Imports and dependencies
- Comments and docstrings
- File name and language
- Code structure (functions, classes)

### Pattern Recognition

The simulator recognizes common patterns:
- Function definition → Suggest docstring
- Class definition → Suggest `__init__`
- Loop comment → Suggest `for` loop
- Validation comment → Suggest `if` statement

## Next Steps

1. **Read the Architecture**: Check out [ARCHITECTURE.md](ARCHITECTURE.md) for a deep dive into how Copilot works
2. **Read the README**: See [README.md](README.md) for complete documentation
3. **Experiment**: Modify the examples to test different scenarios
4. **Learn More**: Understand how real Copilot differs from this simulation

## Tips for Learning

1. Start with `verbose=False` to see just the suggestions
2. Turn on `verbose=True` to understand the process
3. Try different code patterns to see how suggestions change
4. Experiment with confidence scores
5. Read the reasoning for each suggestion

## Common Questions

**Q: Is this the actual GitHub Copilot?**
A: No, this is a simplified educational simulation. Real Copilot uses advanced ML models.

**Q: Can I use this for actual code completion?**
A: This is for learning purposes. Use GitHub Copilot for real code assistance.

**Q: How accurate is the simulation?**
A: It demonstrates the core concepts accurately but simplifies the ML aspects.

**Q: Does it support other languages?**
A: The examples are Python-focused, but the concepts apply to all languages.

## Troubleshooting

**Issue**: `ModuleNotFoundError: No module named 'copilot_simulator'`
**Solution**: Make sure you're running from the correct directory or add the parent directory to your Python path.

**Issue**: Examples don't run
**Solution**: Make sure you're using Python 3.7+

**Issue**: Want to add more patterns
**Solution**: Modify the `patterns` dictionary in the `SuggestionEngine` class

## Contributing

Feel free to:
- Add more pattern recognition examples
- Improve the documentation
- Create new example scenarios
- Enhance the simulation accuracy

## Resources

- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [OpenAI Codex](https://openai.com/blog/openai-codex)
- [ARCHITECTURE.md](ARCHITECTURE.md) - Deep dive into internals

---

Happy learning! 🚀
