# README file

## Birds network: quick description

The birds network project import a JSON file containing Meliza lab gracula birds colony database and use it
as a dataset for python modules called Networkxx and Pyvis in order to plot a dynamic version of a pedigree 
out of it.

![example of a network built with network pyvis](https://pyvis.readthedocs.io/en/latest/_images/net2.png)
This is an example of a network built with NetworkX Pyvis.

## Installation

You will need a version of  Python3.9 installed on your linux operating system. Install pyenv to your linux operating system if
you need to install a virtual environment on Python3.9 and you run a newer version on your machine:

## Installing Pyenv with a Python 3.9 environment
1) For Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python3-openssl git

curl https://pyenv.run | bash
```

Make sure to add the following lines to your shell configuration file (e.g., .bashrc, .zshrc or .bash_profile) to initialize pyenv:
```bash
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

Then, restart your terminal or source the file:
```bash
source ~/.bashrc  # or ~/.zshrc, ~/.bash_profile, depending on your shell
```

2) Now, you can install Python 3.9 using pyenv:
```bash
pyenv install 3.9.10  # or any available 3.9.x version
```

This command will install the specified version of Python. You can check the available Python versions by running:
```bash
pyenv install --list
```

3) Set Python 3.9 as the Local Version:
```bash
pyenv local 3.9.10  # or the version you installed
```
This sets the Python version only for the current directory (project folder). You can also set it globally (for all projects) by using:
```bash
pyenv global 3.9.10
```

4) Now that Python 3.9 is installed, you can create a virtual environment with pyenv-virtualenv. If you don't have pyenv-virtualenv installed, you can install it by running:
```bash
pyenv install pyenv-virtualenv
```
To create a virtual environment with Python 3.9, run:
```bash
pyenv virtualenv 3.9.10 myenv
```
5) To activate the newly created virtual environment, run:
```bash
pyenv activate myenv
```

### Create a python virtual environment with the necessary packages 
1) In the project folder, create a virtual 
environment.

```bash
python -m venv venv
```

2) Activate the python virtual environment and install python modules from the 'requirements.txt' list.

```bash
source venv/bin/activate
python -m pip install -r requirements.txt
```

3) Use Jupyter lab/notebook to vizualize an detailed example of the script.

## Scripts
A) Output a sum_up of selected birds and a mastersheet of the colony.
1) Change the content of the input lis in "./input/list_input.csv".

2) Run the following:
```bash
source venv/bin/activate
cd scripts/
python pedegree_sumup.py
```

3) Retrieve your .csv files in "./output".

### Kinship analysis with PyAGH
PyAGH is a MIT Licenced github project developped for calculating relashinship matrix using pedigree, genotype or microbiology data as well as for processing, analysis and visualization for data.
More information at: https://github.com/zhaow-01/PyAGH
![example of a heatmap built with PyAGH](https://raw.githubusercontent.com/zhaow-01/PyAGH/main/picture/heat_example.png)
PyAGH is used in this project for building relationship matrices. A notebook is available in ./notebooks/husbandry.ipynb
![example of a Pedigree Dendrogram built with PyAGH](https://raw.githubusercontent.com/zhaow-01/PyAGH/main/picture/cluster_example.png)

## Next updates

The goal is to change the form of the node depending on the sex of the bird, the color for alive birds and 
directionality from parents to offspring using arrows.

