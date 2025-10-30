# DataClean CLI

Lightweight Python command-line tool for quick data inspection and preprocessing.
Implemented modular CLI architecture (argparse) and packaging with pyproject.toml.
Designed for reproducible local installation via uv pip install -e .

## Installation

```
git clone https://github.com/anushacodes/mini-datacleaning-cli.git
uv pip install -e .
````

## Usage

### View first few rows

```bash
uv run dataz --i path/to/data.csv --view
```

### Summarize dataset

```bash
uv run dataz --i path/to/data.csv --summarize
```


## Requirements

* Python 3.10+
* uv (for dependency management)



