# Welcome to a basic Python Training Repo!

This repo will show you how to structure a Python project and how to package it.
It will include example scripts that will cover the basics for coding with Python (data types, data structures, functions, classes, etc.).

**Important notes**:
- This repo assumes you are using a Windows computer. Though most of the same stuff should apply for Linux/Mac.
- I use Microsoft Visual Studio Code (VSC) as my go-to text editor. Feel free to use whatever you want, but there may be references to shortcuts that will only work on VSC.
- This project uses `Poetry` as its package manager. Check it out [here](https://python-poetry.org/).
- I am assuming you are very inexperienced with coding, so I will do my best to explain *everything*.


With that out of the way, let's see what you need to do to get started!

----
## Getting Started 

🐍 **Step 1** Download and install Python.
1. Find a version of Python you'd like to install [here](https://www.python.org/downloads/). I recommend 3.10.X and above.
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
