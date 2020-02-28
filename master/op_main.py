#!/usr/bin/python2
# -*- coding: utf-8 -*-
"""
Scripts that acts as a main and executable for calculating order paramater.

Usage:
    python2 op_main.py
    ./op_main.py

Requirement:
    python2.7
    collections
    
    interface.py
    op_traj_mpi.py
"""
from collections import OrderedDict

from interface import interface
from op_traj_mpi import open_trajectory

def main():

    options = OrderedDict( [ ('nprocs',1) , 
                            ('rank',0) , 
                            ('first_frame',-2500) , 
                            ('last_frame',-1) , 
                            ('wrap',True) , 
                            ('visualize',False) , 
                            ('ini_layer_spacing',35.) , 
                            ('gb_type',3) , 
                            ('gb_ends_type',2) , 
                            ('atoms_per_monomer',23) , 
                            ('number_of_monomer',800) , 
                            ('number_of_chains',100) , 
                            ('file_pattern','ellipsoid.*.dump.gz')
                            ] )
    
    run_flag, options = interface(options)

    if run_flag:

        open_trajectory(nprocs=options['nprocs'],
                        rank=options['rank'],
                        first_frame=options['first_frame'],
                        last_frame=options['last_frame'],
                        wrap=options['wrap'],
                        visualize=options['visualize'],
                        ini_layer_spacing=options['ini_layer_spacing'],
                        gb_type=options['gb_type'],
                        gb_ends_type=options['gb_ends_type'],
                        atoms_per_monomer=options['atoms_per_monomer'],
                        number_of_monomer=options['number_of_monomer'],
                        number_of_chains=options['number_of_chains'],
                        file_pattern=options['file_pattern']
                        )
    else:
        print("Exiting script...")

main()
