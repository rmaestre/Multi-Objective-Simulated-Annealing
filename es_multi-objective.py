#! /usr/bin/python
# -*- coding: utf-8 -*-
import math
import random

# Number of districts
districts_number = 16
maximun_bomber_in_district = 1

# Districts neighbors
neighbors = {}
neighbors[1] = [1, 2 , 4 , 5]
neighbors[2] = [2, 1 , 3 , 5 , 6]
neighbors[3] = [3 , 2 , 6 , 7]
neighbors[4] = [4 , 1 , 5 , 8 , 10 , 11]
neighbors[5] = [5 , 1 , 2 , 4 , 6 , 8]
neighbors[6] = [6 , 2 , 3 , 5 , 7 , 8 , 9]
neighbors[7] = [7 , 3 , 6 , 9 , 13]
neighbors[8] = [8 , 4 , 5 , 6 , 9 , 11 , 12]
neighbors[9] = [9 , 6 , 7 , 8 , 12 , 13]
neighbors[10] = [10 , 4 , 11 , 14]
neighbors[11] = [11 , 4 , 8 , 10 , 12 , 14 , 15]
neighbors[12] = [12 , 8 , 9 , 11 , 13 , 14 , 15]
neighbors[13] = [13 , 7 , 9 , 12 , 15 , 16]
neighbors[14] = [14 , 10 , 11 , 12 , 15]
neighbors[15] = [15 , 11 , 12 , 13 , 14 , 16]
neighbors[16] = [16 , 13 , 15]

def districtsCoverBySomeSolution(stations):
    """
    Calculate the number of districts cover by one solution
    Given a bomber station (for each one), return all adjacent neighbors.
    """
    districts_cover = dict()
    cent = False
    cont = 0
    while cont < len(stations):
        # Itself is cover
        if stations[cont] > 0:
            districts_cover[cont+1] = True
            # Get all neighbors from station-district location
            #print cont+1,' ',neighbors[cont+1]
            for distrito in neighbors[cont+1]:
                districts_cover[distrito] = True
                # Exit loop if all districts all cover
                if len(districts_cover) == districts_number:
                    cent = True
        cont += 1
    return districts_cover
    
def f1(solution):
    """
    WE SHOULD TO MAXIMIZE (but invert the sign)
    This function calculate the districts cover by one vector of solution.
    This vector is the index where bombers has a station.
    """
    return - float(len(districtsCoverBySomeSolution(solution)))
    
def f2(solution):
    """
    WE SHOULD TO MINIMIZE
    Calculate the number of bomber stations
    """
    return sum(solution)
    

def generateRandSolution(x = None):
    """
    Generate a vector with random values
    If x is None, this function create one new random vector,
    if it is not, copy x vector and permut two position in order
    to get a new individual of x entorn.
    """
    solution = []
    if x == None:
        for i in range(1, districts_number + 1):
            solution.append(random.randrange(0 , maximun_bomber_in_district + 1))
    else:
        for i in x:
            solution.append(i)
        n = len(solution)
        # Apply two random transformations in two positions in order to
        # get a "near" new solution
        for i in range(0 , 2):
            rand_index = random.randrange(0 , n)
            # 0.5 of propability in each branch
            if random.random() < 0.5:
                solution[rand_index] =  1
            else:
                solution[rand_index] =  0
            # Check if values are in range [0 .. N]
            if solution[rand_index] < 0:
                solution[rand_index] = 0
            elif solution[rand_index] > maximun_bomber_in_district:
                solution[rand_index] = maximun_bomber_in_district
    return solution
    
    
def update_pe_list(new_solution , PE):
    """
    Delete dominate solutions, and check if i can append the new solution to the PE
    """
    ns_f1 = f1(new_solution)
    ns_f2 = f2(new_solution)
    dominatedByOtherSolution = False
    # Search if a solution in a PE vector is dominated by
    for solution in PE:
        s_f1 = f1(solution)
        s_f2 = f2(solution)
        # Check if it is dominated
        if (ns_f1 <= s_f1 and ns_f2 < s_f2  or 
            ns_f1 < s_f1  and ns_f2 <= s_f2 or 
            ns_f1 < s_f1  and ns_f2 < s_f2    ):
            PE.remove(solution)
        # and if is it is not dominated by a value ina a PE vector
        elif (s_f1 <= ns_f1 and s_f2 <= ns_f2):
            dominatedByOtherSolution = True
    # Append to PE border if it is legal
    if not dominatedByOtherSolution and y not in PE:
        PE.append(new_solution)
    return PE


# General algorithm parameters    
params = {}
# Initial temperature
params['temperature'] = 100.0
# Cooling factor
params['alpha'] = 0.9
# Steps number keeping the temperature
params['np'] = 30
# Final temperature
params['final_temperature'] = 0.01
# Number of iterations without improving
params['number_iterations_without_improves'] = 3000
# Total number of iterations
params['nnum'] = 0

# Pareto border
PE = []

# Files to save de temperature decrement and f1,f2 values
fd = file('/tmp/data' , 'w')
fd_tempe = file('/tmp/data_temperatura' , 'w')

# Generate random initial solution 
x = generateRandSolution()

PE.append(x)
n = 0
# Start the algorithm

while (params['temperature'] > params['final_temperature'] and
        params['nnum'] < params['number_iterations_without_improves']):
    # Get solution of x entorn
    y = generateRandSolution(x)

    # Calculate distance between two solutions
    delta = (f1(y) - f1(x)) + (f2(y) - f2(x))
    # If delta is better, accept new solution
    if delta < 0.0:
        PE = update_pe_list(y , PE)
        x = []
        x.extend(y)
    # If it is not better, compute probabilities to accept other solutions
    else:
        if (random.random() < math.exp(- float(delta) / params['temperature'])):
            PE = update_pe_list(y , PE)
            x = []
            x.extend(y)
    # Low temperature
    if params['nnum'] % params['np'] == 0:
        params['temperature'] *= params['alpha']
        # Save temperature decrement
        fd_tempe.write('%s\n' % params['temperature'])
    params['nnum'] += 1
    
    # Save data ina file
    fd.write('%s\t%s\n' % (f1(x) , f2(x)))
    
    # Print temperature
    print 'Tº: %s' % params['temperature']
    

# Finally print the pareto border with all optimal solutions.
print '\nSolution/s: '
for p in PE:
    # If this solution is legal
    if f1(p) == -16:
        # Print solution
        print p,
        cont = 0
        # Print readble representation of the vector
        print 'Stations: ',
        while cont < len(p):
            if p[cont] == 1:
                print (cont+1),
            cont += 1
        # Print function values
        print '\nF1:%d F2:%d' % (f1(p) , f2(p))
        print ''