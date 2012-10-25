# Introduction

The classic paper can be found here: http://home.gwu.edu/~stroud/classics/KirkpatrickGelattVecchi83.pdf

(From wikipedia http://en.wikipedia.org/wiki/Simulated_annealing)

Simulated annealing (SA) is a generic probabilistic metaheuristic for the global optimization problem of locating a good approximation to the global optimum of a given function in a large search space. It is often used when the search space is discrete (e.g., all tours that visit a given set of cities). For certain problems, simulated annealing may be more efficient than exhaustive enumeration — provided that the goal is merely to find an acceptably good solution in a fixed amount of time, rather than the best possible solution.

The name and inspiration come from annealing in metallurgy, a technique involving heating and controlled cooling of a material to increase the size of its crystals and reduce their defects. The heat causes the atoms to become unstuck from their initial positions (a local minimum of the internal energy) and wander randomly through states of higher energy; the slow cooling gives them more chances of finding configurations with lower internal energy than the initial one.
By analogy with this physical process, each step of the SA algorithm attempts to replace the current solution by a random solution (chosen according to a candidate distribution, often constructed to sample from solutions near the current solution). The new solution may then be accepted with a probability that depends both on the difference between the corresponding function values and also on a global parameter T (called the temperature), that is gradually decreased during the process. The dependency is such that the choice between the previous and current solution is almost random when T is large, but increasingly selects the better or "downhill" solution (for a minimization problem) as T goes to zero. The allowance for "uphill" moves potentially saves the method from becoming stuck at local optima—which are the bane of greedy algorithms.

# Sample problem

![function1](https://raw.github.com/rmaestre/Multi-Objective-Simulated-Annealing/master/img/districts.png)

We should place several people on the board trying to cover the whole space, fulfilling the following rules:

* If there is an agent on position #5, positions: #5, #1,#2,#4,#6 and #8 are covered.
* We should use the minimum number of people

# Functions

![function1](https://raw.github.com/rmaestre/Multi-Objective-Simulated-Annealing/master/img/function1.png)

![function2](https://raw.github.com/rmaestre/Multi-Objective-Simulated-Annealing/master/img/function2.png)

![function3](https://raw.github.com/rmaestre/Multi-Objective-Simulated-Annealing/master/img/function3.png)

# Uni-objective approach convergence

![function1](https://raw.github.com/rmaestre/Multi-Objective-Simulated-Annealing/master/img/convergence_uni.png)

# Multi-objective approach convergence

![function1](https://raw.github.com/rmaestre/Multi-Objective-Simulated-Annealing/master/img/convergence_multi.png)