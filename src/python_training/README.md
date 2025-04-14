# Welcome to the actual training folders!
You are currently in the `src` folder/directory.

As a quick recap, we will cover the following:
- 01_basics
- 02_control_flow
- 03_functions
- 04_oop_and_classes

This directory also has a `main.py`, which serves as the entry point for the `python_training` package. When you run the script, it will:
- Parse arguments passed to the script (using `argparse`).
- If the `--ascii_print` flag is passed, it will print some ASCII art.

Example of how to run it:

```bash
python main.py --ascii_print
```

## How to make a Python package of this repo.
A Python package is a way to distribute and reuse code. Packages essentially work like any other library (like when we do `import os`, but instead it will be whatever we name our package -> `import python_training`). This gives other code access to all the code we've written!


Everything under `src/` will be packaged (this is usually how it goes for most projects). That means all files outside of this directory will not be in the package.

To package this repo with Poetry, follow these steps:

1. **Ensure the structure**: Place all your Python files under the `src/` directory (which is common for most projects).

2. **Configure `pyproject.toml`**: Make sure it includes your dependencies, package configuration, and scripts (as seen in the example provided).

3. **Build the package**: Run the following command to build the package:
```bash
poetry build
```

This will create a .whl and .tar.gz file, ready for distribution or installation.
This can be done with `pip`:
```bash
pip install ./python_training-0.1.0-py3-none-any.whl
```


## What is a __init__.py?
The `__init__.py` file is used to mark a directory as a Python package. When this file is present in a directory, Python
will treat the directory as a package, and you can import modules from that directory. It's not strictly necessary for
every package, but it helps manage the package structure.


## Things we won't cover.
As this is an intro for beginners, there are things we won't be covering.
However, I encourage you to look into them once you finish this!

- [Async Programming](https://realpython.com/async-io-python/)
- [APIs](https://realpython.com/api-integration-in-python/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- And more advanced topics.
