# TSP - MOG

In this repository we store every documentation file including code files that we have used to introduce our classmates to the Travelling Salesman Problem as an optional special assignment for a subject called *Operational Models of Management*(originally, MOG).

You can directly jump to the [slides](slides.pdf) or read the [full documentation](tsp.pdf) that the slides are based on. Both have been written in spanish  because of a language constraint in the assignment for the subject

## Travelling Salesman Problem 🏙

The travelling salesman problem (TSP) asks the following question: _"Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city and returns to the origin city?"_

## Implementation 💻

We have implemented two solutions to the Travelling Salesman Problem using [C++(branch and bound)](branch-bound.cpp) and [Python(nearest neighbour)](tsp.py)

## Running our TSP Python implementation locally 🏠

Clone this repository by running the following command in a terminal capable of running _git_: `git clone https://github.com/albertopastormr/tsp-mog.git`.

Install all the requirements by following [the guide below](https://github.com/albertopastormr/tsp-mog#requirements-%EF%B8%8F).

Run `tsp.py` by running the following command in a terminal capable of running _python_: `python3 tsp.py`. It should return the optimal path in a matplotlib graph.

## Requirements ⚙️

Besides [Python 3.6](https://www.python.org/downloads/) we will be using the following packages:

* [numpy](http://www.numpy.org/)
* [scipy](https://www.scipy.org/)
* [matplotlib](https://matplotlib.org/) 
* [networkx](https://networkx.github.io/)

You can simply install each package using `pip` as follows:
```bash
pip install <package>
```

Or you can install all the packages needed with the [`requirements.txt`](requirements.txt) file by running:
```bash
pip install -r requirements.txt
```
