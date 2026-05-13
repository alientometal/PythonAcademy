# Development Environment Setup

This repository is configured to run in **GitHub Codespaces** or any VS Code Dev Container environment.

## Launching the Environment

1. Click on the **Code** button in GitHub and select **Create codespace on main**.
2. Wait for the container to build. The `postCreateCommand` will automatically install all necessary Python dependencies and set up the `trainings` kernel.

## Jupyter Notebooks

To start a Jupyter session from the terminal:
```bash
jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root
```
*Note: VS Code will automatically detect Jupyter files (.ipynb) and allow you to run them using the `trainings` kernel without manually starting the lab server.*

## Connecting to PostgreSQL

### From psql CLI
In the terminal, run:
```bash
psql -h $POSTGRES_HOST -U $POSTGRES_USER -d $POSTGRES_DB
```
(Password: `trainings`)

### From a Python Notebook (SQLAlchemy)
Use the following connection template:

```python
import os
from sqlalchemy import create_url, create_engine

# Connection details from environment variables
user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
host = os.getenv("POSTGRES_HOST")
port = os.getenv("POSTGRES_PORT")
db = os.getenv("POSTGRES_DB")

url = f"postgresql://{user}:{password}@{host}:{port}/{db}"
engine = create_engine(url)

# Example: Read a table
# import pandas as pd
# df = pd.read_sql("SELECT * FROM my_table", engine)
```

## Copilot "Hint Mode"
This environment is configured to reduce GitHub Copilot's auto-solve behavior.

- Automatic inline completions are disabled.
- Next edit suggestions are disabled.
- Copilot Chat should behave like a TA, not a solution generator.
- For notebooks, TODOs, exercise prompts, starter code, and assert/check cells, Copilot should give hints, questions, pseudocode, or very small fragments instead of full completed answers.
- Students should still write the final code themselves and use the notebook assert/check cells to verify progress.

The detailed behavior rules live in [`.github/copilot-instructions.md`](./.github/copilot-instructions.md).
