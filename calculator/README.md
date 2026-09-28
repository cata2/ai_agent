# Calculator

A simple command-line calculator application that evaluates arithmetic expressions with operator precedence. Written in Python with type hints and unit tests.

## Features

- **Basic arithmetic operations**: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`)
- **Operator precedence**: Multiplication and division are evaluated before addition and subtraction
- **Command-line interface**: Pass expressions directly as arguments
- **JSON output**: Results are formatted as JSON for easy parsing
- **Type hints**: Full type annotation support
- **Unit tests**: Comprehensive test suite using `unittest`

## Project Structure

```
calculator/
├── main.py              # Entry point for the CLI application
├── tests.py             # Unit tests for the Calculator class
├── pkg/
│   ├── calculator.py    # Core Calculator class implementation
│   └── render.py        # JSON output formatting utility
└── README.md            # This file
```

## Installation

No installation required. Simply clone or download the project and run it with Python 3.

```bash
git clone https://github.com/yourusername/calculator.git
cd calculator
```

## Usage

### Command Line

Run the calculator from the command line by passing an expression as an argument:

```bash
python main.py "3 + 5"
python main.py "10 - 4"
python main.py "3 * 4"
python main.py "10 / 2"
```

You can also use complex expressions with operator precedence:

```bash
python main.py "3 * 4 + 5"
python main.py "2 * 3 - 8 / 2 + 5"
```

### Output Format

The calculator returns results in JSON format:

```json
{
  "expression": "3 + 5",
  "result": 8
}
```

### Running Without Arguments

When run without arguments, the calculator displays a helpful usage message:

```bash
python main.py
```

Output:
```
Calculator App
Usage: python main.py "<expression>"
Example: python main.py "3 + 5"
```

## Programmatic Use

You can also use the `Calculator` class directly in your Python code:

```python
from pkg.calculator import Calculator

calc = Calculator()
result = calc.evaluate("3 + 5")
print(result)  # Output: 8.0
```

## Supported Operators

| Operator | Description | Precedence |
|----------|-------------|------------|
| `+`      | Addition    | Low (1)    |
| `-`      | Subtraction | Low (1)    |
| `*`      | Multiplication | High (2) |
| `/`      | Division    | High (2)   |

## Error Handling

The calculator handles various error conditions gracefully:

- **Invalid tokens**: Raises `ValueError` for non-numeric or unsupported operators
- **Insufficient operands**: Raises `ValueError` when an operator lacks operands
- **Empty expressions**: Returns `None` for empty or whitespace-only input
- **Division by zero**: Will raise a `ZeroDivisionError` (Python built-in)

## Testing

Run the test suite to verify the calculator works correctly:

```bash
python -m unittest tests.py
```

Or run the tests file directly:

```bash
python tests.py
```

The test suite covers:
- Basic arithmetic operations (addition, subtraction, multiplication, division)
- Complex expressions with operator precedence
- Edge cases (empty expressions, invalid operators, insufficient operands)

## License

MIT License