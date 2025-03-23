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
The following are brief descriptions of each directory and file in the repo (shown with hierarchy):
```
📦 python_training # the root directory (and name of the repo)
├── 📂 src                          # Contains the main source code (only these contents get packaged)
│   ├── 📂 python_training          # Python training scripts and modules (name of the package)
|   |   ├── 📂 01_basics            # Contains script examples going over variables, data types, and data structures
|   |   ├── 📂 02_control_flow      # Contains script examples going over logical expressions and loops
|   |   ├── 📂 03_functions         # Contains script examples going over functions (reusable code)
|   |   ├── 📂 04_oop_and_classes   # Contains script examples going over OOP fundamentals and classes
│   │   ├── main.py                 # The main script for the package (has an entry point defined in the toml)
│   │   ├── ascii_art.py            # Contains ASCII art for examples
│   |   ├── __init__.py             # Marks this as a package (allows for imports -> this is needed for all directories that need to be imported)
├── 📂 users                        # The users directory where anyone can make changes
│   ├── 📂 example_user             # Tests for the training script
│   |   ├── example.py              # A user's script
├── 📂 coding_problems              # Contains challenges to practice what you've learned
│   ├── 📂 register_access          # A project to validate a memory mapped register access using indirect access
│   |   ├── sort_by_password.py     # A good exercise to better grasp lists and dicts
├── 📄 README.md                    # Project documentation (what you're reading now!)
├── 📄 CHANGELOG.yaml               # Tracks changes per release of the package
├── 📄 .gitignore                   # Files to ignore in git (these don't get added to the repo)
├── 📄 poetry.lock                  # Contains all the dependencies for the Poetry virtual environment (these are locked by version)
├── 📄 pyproject.toml               # The main configuration file for the package (defines dependencies, metadata, etc.)
├── 📄 .pre-commit-config.yaml      # Defines what gets ran prior to making a commit
├── 📄 vscode_tips.md               # Tips and tricks for VS Code
```
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
I highly encourage users to practice the git process. In the spirit of enabling this, I've set up a `users` directory where anyone can submit their example code.
If you're completely unfamiliar with git, check out the [documentation](https://www.atlassian.com/git)!

For beginners, most changes follow this order:
```bash
git pull # grab all changes/branches from the repo; important for ensuring the local branch has updated info
git checkout <branch name> # enter the name of the branch to switch to (needs to exist)
git pull # [optional] pull all changes on that specific branch
git add -A # add all changes to the staging area
git commit -m "<Commit summary here (explain the changes)>" # create a commit
git push # push the changes to the remote branch (on GitHub)
```

**Note:** Before making any changes, I recommend doing a `git pull` to avoid headaches with merge conflicts...But if you already have changes, it might be good idea to do a `git stash` first. Once the latest changes are pulled, then reload your changes with `git stash pop`.

> [!TIP]
>Since this repo uses `pre-commit`, submitted code will be validated and formatted automatically. So don't worry too much about formatting things yourself (just be sure to get used to how the code gets formatted).

The master branch is pull-request (PR) protected, which means anyone trying to merge changes **must create a pull-request and follow the code review process**. Additionally, there will be continuous integration (CI) pipelines implemented through [`GitHub Actions`](https://docs.github.com/en/actions) that will do all the same checks as pre-commit (in case someone forgets to do `pre-commit install`). If these checks do not pass, then PRs won't be allowed to be merged.
