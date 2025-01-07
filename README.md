# AdventOfCode

Repository for Adevent of Code

Written in `Python`

Solutions presented are not always the first solve, I aim to first solve the puzzle and then clean up the code to be more redable.

From project root:
Run `export PYTHONPATH=$(pwd)` if you experience ModuleNotFoundError when importing functions from local files

For debugging, add the following to the top of the file:
```py
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
```

Run `python scripts/generate_day_file.py <year> <day>` to generate boilerplate code for a given new day
