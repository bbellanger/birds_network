# README file

## Birds network: quick description

The birds network project import a JSON file containing Meliza lab gracula birds colony database and use it
as a dataset for python modules called Networkxx and Pyvis in order to plot a dynamic version of a pedigree 
out of it.

![example of a network built with network pyvis](https://pyvis.readthedocs.io/en/latest/_images/net2.png)
This is an example of a network built with NetworkX Pyvis.

## Installation

1) You will need Python3 installed on your linux operating system.

2) In the project folder, create a virtual 
environment.

```bash
python -m venv venv
```

3) Activate the python virtual environment and install python modules from the 'requirements.txt' list.

```bash
source venv/bin/activate
python -m pip install -r requirements.txt
```

4) Use Jupyter lab/notebook to vizualize an detailed example of the script.

## Next updates

The goal is to change the form of the node depending on the sex of the bird, the color for alive birds and 
directionality from parents to offspring using arrows.
