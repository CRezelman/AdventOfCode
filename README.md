# Advent of Code

Solutions for Advent of Code, written in Python.

The aim of this repository is to solve each puzzle first, then clean and refine the code into something readable and reusable.
Utilities and solvers live in the src/ directory.

## Project Structure
```css
AdventOfCode/
│
├── src/
│   ├── utilities/
│   └── ... (shared solver code)
│
├── 2025/
│   ├── Day1.py
│   ├── Day2.py
│   └── ...
│
├── scripts/
│   └── generate_day_file.py
│
└── README.md
```

## Virtual Environment

It’s recommended to run Advent of Code inside a Python virtual environment.

Create a venv
```bash
python -m venv .venv
```

Activate the venv

```bash
source .venv/Scripts/activate
```


Install dependencies
```bash
pip install -r requirements.txt
```

## Installing the src package (editable mode)

The project uses a src/ layout, so install it locally in editable mode:
```bash
pip install -e .
```

This allows you to import modules like:
```py
from utilities.solver import Solver
```

without adjusting sys.path.

## Generating Day Boilerplate

To create a new year/day file with starter code:

```py
python scripts/generate_day_file.py <year> <day>
```

Example:

```py
python scripts/generate_day_file.py 2025 3
```

## Running a Day

Each day file can be run directly:

```py
python -m 2025.Day3
```

Your base Solver class handles:

- input loading
- timing
- styled output via Rich

## Debugging in VS Code

When using the .venv interpreter, VS Code handles imports automatically.
Just ensure you've selected the correct interpreter:

Ctrl + Shift + P → “Python: Select Interpreter” → choose the .venv one
