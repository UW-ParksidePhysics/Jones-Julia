#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 09:05:29 2020

@author: julia
"""

###Final Exam###


from numpy import linspace, array 
import matplotlib.pyplot as mp

from two_column_text_read_12 import two_column_text_read
from univariate_statistics_12 import univariate_statistics
from quadratic_fit_12 import quadratic_fit
from equations_of_state import fit_eos

from generate_matrix import generate_matrix
from lowest_eigenvectors_12 import lowest_eigenvectors

filename="Si.Fd-3m.GGA-PBEsol.volumes_energies.dat"
my_eos='vinet'
n_dimensions=90
potential_name='square'
potential_parameter=300
display_graph=True

#Part 1

#1
def parse_file_name(filename):
    """ Extract the chemical symbol (CS), crystal symmetry symbol (CSS), 
    and density functional exchange-correlation approximation
    acronym (AA) for the given file name.
    """
    to_parse=filename.split(".")
    CS, CSS, AA = to_parse[0:3]
    return CS, CSS, AA

CS, CSS, AA = parse_file_name(filename)

#2
data = two_column_text_read(filename) 

#3
""" Dr. Parker and I figured out we must divde data by two later on. """
    
#4
statistics = univariate_statistics(data)

#5
quadratic_coefficients = quadratic_fit(data)

#6
""" Must reformat data before finding fit curve. """
un_data = zip(*data)
data_2 = list(un_data)

volumes=data_2[0]
energies= data_2[1]

eos_fit_curve, bulk_modulus= fit_eos(volumes, energies, quadratic_coefficients, eos=my_eos)

#7
"""  Convert units module """
def convert_units(value_to_be_converted, units_of_value_to_be_converted_from, units_to_be_converted_to):
    """
    :param value_to_be_converted: Somevalue
    :param units_of_the_value_to_be_converted_from: Accepted units: cb/a, rb/a, rb/cb
    :param units_to_be_converted_to: Accepted units: ca/a, ev/a, GPa
    :return: value_in_the_requested_units
    """
    if units_of_value_to_be_converted_from == "cb/a":
        value_in_requested_units = value_to_be_converted * 0.148185, units_to_be_converted_to
    
    elif units_of_value_to_be_converted_from == "rb/a":
        value_in_requested_units = value_to_be_converted * 13.6057, units_to_be_converted_to
    elif units_of_value_to_be_converted_from == "rb/cb":
        value_in_requested_units = value_to_be_converted / 29421.02648438959, units_to_be_converted_to
    else:
        value_in_requested_units = value_to_be_converted
    return value_in_requested_units

""" Convert bulk_modulus to GPa """
value_to_be_converted=bulk_modulus
units_of_value_to_be_converted_from="rb/cb"
units_to_be_converted_to="GPa"

bulk_modulus, units = convert_units(value_to_be_converted, units_of_value_to_be_converted_from, units_to_be_converted_to)

#8
""" We can now divide data and eos_fit_curve by two, but we must convert data to an array first.
Then we reformat back to list.
Plot data and fit curve, x and y limits, and title.
"""
data_2=array(data_2)
data_2=data_2/2
eos_fit_curve=eos_fit_curve/2

fig = mp.figure()
ax=fig.add_subplot(111)

data_list=list()
data_list=data_2.tolist()

volumes = linspace(min(data_list[0]), max(data_list[0]), len(eos_fit_curve))
line1, = ax.plot(data_list[0], data_list[1], 'o')
line2, = ax.plot(volumes, eos_fit_curve, color="black")


x_min = (min(data_list[0]) - (min(data_list[0]) * 0.10))
x_max = (max(data_list[0]) + (max(data_list[0]) * 0.10))
y_min = (min(data_list[1]) - (min(data_list[0]) * 0.000010))
y_max = (max(data_list[1]) + (max(data_list[0]) * 0.000010))

mp.xlim(x_min, x_max)
mp.ylim(y_min, y_max)
mp.xlabel(r' $V$ $ \mathit{Å^3/atom}\ $')
mp.ylabel(r' $E$ $ \mathcal{eV/atom}\ $')

#9 

def annotate_graph(CS, CSS):
    """ Returns annotations for the CS, CSS, K_0 and V_0.
    Also draws a vertical line at the equilibrium point and adds title and signature.
    xy location is a lot of hard coding because I couldnt figure out how else to do it.
   :param CS:              str :: from number one
   :param CSS:             str :: from number one
   """
   
    ax.annotate(CS, xy= ((x_min + 3), max(data_list[1])))
    
    ax.annotate('$ {}\overline{{{}}} {}$'.format(CSS[0:2], 
                                            CSS[3], 
                                            CSS[1]),
        xy=(equilibrium_volume, (max(data_list[1])-0.001)))
        
    ax.annotate('K_0={:.6f}{}'.format(bulk_modulus, units),
             xy=(equilibrium_volume, max(data_list[1])))
    
    
    ax.annotate('V_0={:.3f}Å^3/atom'.format(equilibrium_volume),
            xy=(equilibrium_volume, (min(data_list[1]))-.0004))
    
    mp.axvline(x=equilibrium_volume,ymin=0, ymax= 0.06, 
            color="black", linestyle='--')
    mp.text(equilibrium_volume, (min(data_list[1]))-.004, "Created by Julia Jones 2020-05-13")
    mp.title("{} Equation of State for {} in {}".format(my_eos, CS, AA))
    return ax, mp

 
equilibrium_volume = data_list[0][data_list[1].index(min(data_list[1]))] 
annotate_graph(CS,CSS)

#10
if display_graph == True:
    mp.show(display_graph)
else:
    mp.savefig("Jones.{}.{}.{}.{}EquationOfState.png".format(CS,CSS, AA, my_eos))

############################################ Part two ##############################################################################


#1
minimum_x=-10
maximum_x=10
matrix = generate_matrix(minimum_x, maximum_x, n_dimensions, potential_name, potential_parameter)
   
#2
square_matrix=matrix
starting_index=3
ending_index=6
eigenvalues,eigenvectors=lowest_eigenvectors(square_matrix, starting_index, ending_index)

#3
x = linspace(-10, 10, n_dimensions)

#4
line1, = mp.plot(x, eigenvectors[0][0:n_dimensions], color='orange')
line2, = mp.plot(x, eigenvectors[1][0:n_dimensions], 'm')
line3, = mp.plot(x, eigenvectors[2][0:n_dimensions], 'c')
mp.xlabel("x [a.u.]")
mp.ylabel("ψn ( x ) [a.u.]")
mp.legend((line1, line2, line3), ('ψ2, Ε2 = 0.18851101 a.u.', 'ψ3, Ε3 = 0.0.29428517 a.u.', 'ψ4, Ε4 = 0.42330764 a.u.'))
mp.axis([-10,10, max(eigenvectors[0]) - 2, max(eigenvectors[0]) + 2])

#5
mp.axhline(color="black")

#6
mp.text(-10, -3, "Created by Julia Jones 2020-05-12")

#7
mp.title("Select Wavefunctions for a {} Potential on a Spatial Grid of {} Points".format(potential_name,n_dimensions))

#8
if display_graph == True:
   mp.show(display_graph)
else:
    mp.savefig("Jones.{}.Eigenvector.index{}to{}.png".format(potential_name, starting_index, ending_index))

