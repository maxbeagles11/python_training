# Welcome to a basic Python training repo!

This repo will show you how to structure a Python project and how to package it.
It will include example scripts that will cover the basics for coding with Python (data types, data structures, functions, classes, etc.).
It will also provide an opportunity to learn how to work with git and collaborating on a project.

**Important notes**:
- This repo assumes you are using a Windows computer. Though most of the same stuff should apply for Linux/Mac.
- I use Microsoft Visual Studio Code (VSC) as my go-to text editor. Feel free to use whatever you want, but there may be references to shortcuts that will only work on VSC.
- This project uses `Poetry` as its package manager. Check it out [here](https://python-poetry.org/).
- I am assuming you are very inexperienced with coding, so I will do my best to explain *everything*.


With that out of the way, let's see what you need to do to get started!

----
## Getting Started

🐍 **Step 1** Download and install Python.
1. Find a version of Python you'd like to install [here](https://www.python.org/downloads/). I recommend 3.10.X and above to run any of the scripts. **Note**: to use the Poetry toml, please install 3.10.X.
2. Pick the Windows 64-bit installer and then run it.
3. Select the default options in the installer.
4. Check your environment variables and add Python and Python/scripts to path (if they're not there already). Here's a [useful guide](https://www.howtogeek.com/787217/how-to-edit-environment-variables-on-windows-10-or-11/) on how to do this.
a Ex: C:\Users\my_user\AppData\Local\Programs\Python\Python313
b Ex: C:\Users\my_user\AppData\Local\Programs\Python\Python313\Scripts
5. Confirm that `python` works in your terminal by running:
```bash
python --version
```

🔧 **Step 2** Install git on your computer.
1. Download the installer from [here](https://git-scm.com/downloads/win).
    a. Make sure you grab the 64-bit installer.
2. Select the default options in the installer.

📥 **Step 3** Open your text editor and clone this repository.
1. There are many ways to do this, but here's what I normally do (this is done in the terminal):
```bash
git clone https://github.com/maxbeagles11/python_training.git
```
2. Once it's installed, change directories to `python_training` by running the following:
```bash
cd python_training
```

📦 **Step 4** Install Poetry.
1. Run:
```bash
pip install poetry
```

🚀 **Step 5** Install all dependencies.
1. Lastly, let's install all the dependencies by running:
```bash
poetry install
```
2. Let's also install pre-commit so we can add some uniformity to all code.
```bash
pre-commit install
```

## Project Structure


## Running Scripts

#### Direct Runs
You can run any Python script from your terminal simply by using the `python` or `py` command followed by the file path to the script.

Let's say we're at the `/src` directory in our terminal and we want to run the `main.py` script. Then we'd run:
```bash
python python_training/main.py <insert arguments here>
```

#### Within the Poetry Venv
Since we're using Poetry in this repo, we can execute scripts from within the virtual environment as well.

Depending on the Poetry version installed, you should be able to launch the venv by running:
```bash
poetry shell
```
Then you can use the `Direct Runs` methods described above.

If you don't want to launch the venv, then you can still run from within it by pre-pending `poetry run` to your Python command:
```bash
poetry run python python_training/main.py <insert arguments here>
```
**Note:** You can also run the entry points (shown below) from within the Poetry virtual environment as well (with either method).

#### Using Entry Points
You can define entry points to your Python package from within the toml. This allows your Python package to be very versatile.
Here are some of the entry points included with this repo's package:
```bash
# Runs the main script
run_main <include arguments here>
```

**Note:** Since we'll be using argparse for all arguments in this repo, we have automatic `help` options, which will print out all available options/arguments for that particular script.
Ex:
```bash
run_main -h
# or
run_main --help
```

## Pushing Changes
