````markdown
# Dataz CLI

Lightweight Python command-line tool for quick data inspection and preprocessing.
Implemented modular CLI architecture (argparse), packaging with pyproject.toml, and data operations using pandas.
Designed for reproducible local installation via uv pip install -e .

## Installation

```
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
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

* Python 3.8+
* pandas
* uv (for dependency management)



