#!/usr/bin/python2
# -*- coding: utf-8 -*-
"""

@author: olivier

This script makes a generic menu for changing fonction arguments out of a dictionnary.

Usage:
run_flag, options = interface(options)
options is an ordered dict. As of python3, dictionnaries are ordered by default.

Requirement:
    python2.7 (altough it doesnt seem to have problems running on python3
    curses
    OrderedDict
"""

import curses
from collections import OrderedDict

menu = OrderedDict()

def print_menu(stdscr, selected_row_idx):
    stdscr.clear()
    h = stdscr.getmaxyx()[0]
    for idx, row in enumerate(menu):
        x_name = 5
        x_value = 25
        y = h//2 - len(menu)//2 + idx
        if idx == selected_row_idx:

            stdscr.attron(curses.color_pair(3))
            stdscr.addstr(y, x_name, row + ' :')
            stdscr.attroff(curses.color_pair(3))
            
            stdscr.attron(curses.color_pair(4))
            stdscr.addstr(y, x_value, str(menu[row]))
            stdscr.attroff(curses.color_pair(4))

        else:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x_name, row + ' :')
            stdscr.attroff(curses.color_pair(1))

            stdscr.attron(curses.color_pair(2))
            stdscr.addstr(y, x_value, str(menu[row]))
            stdscr.attroff(curses.color_pair(2))
            
    stdscr.refresh()

def status_bar(stdscr, str):
    h, w = stdscr.getmaxyx()

    stdscr.attron(curses.color_pair(5))
    stdscr.addstr(h-1, 0, str)
    stdscr.addstr(h-1, len(str), " " * (w - len(str) - 1) )
    stdscr.attroff(curses.color_pair(5))
    
    stdscr.refresh()

def edit_options(stdscr,row):
    h, w = stdscr.getmaxyx()
    
    y = h//2 - len(menu)//2 + row
    x = 25

    curses.echo()
    
    curses.setsyx(y,x)
    for _ in range(x,w):
        stdscr.delch(y,x)

    status_bar(stdscr, 'Enter setting value')
    new_setting = stdscr.getstr(y,x)
    
    curses.noecho()

    row_edit = list(menu.keys())[row]

## Should be put in a more compact format
################################################################################################
    if row_edit == 'nprocs':
        try:
            menu[row_edit] = int(new_setting)
            status_bar(stdscr, row_edit+' saved succesfully. Press any key to continue')
        except ValueError:
            status_bar(stdscr, 'Error, any key to continue. nprocs is the number of processor. Leave to 1 for no mpi. Type : int')
    
    elif row_edit == 'rank':
        try:
            menu[row_edit] = int(new_setting)
            status_bar(stdscr, row_edit+' saved succesfully. Press any key to continue')
        except ValueError:
            status_bar(stdscr, 'Error, any key to continue. rank is the number of mpi ranks. Type : int')

    elif row_edit == 'first_frame':
        try:
            menu[row_edit] = int(new_setting)
            status_bar(stdscr, row_edit+' saved succesfully. Press any key to continue')
        except ValueError:
            status_bar(stdscr, 'Error, any key to continue. Negative int. Type : int')

    elif row_edit == 'last_frame':
        try:
            menu[row_edit] = int(new_setting)
            status_bar(stdscr, row_edit+' saved succesfully. Press any key to continue')
        except ValueError:
            status_bar(stdscr, 'Error, any key to continue. Negative int. Type : int')

    elif row_edit == 'wrap':
        try:
            menu[row_edit] = bool(new_setting)
            status_bar(stdscr, row_edit+' saved succesfully. Press any key to continue')
        except ValueError:
            status_bar(stdscr, 'Error, any key to continue. Wraps dump lines. Type : bool')

    elif row_edit == 'visualize':
        try:
            menu[row_edit] = bool(new_setting)
            status_bar(stdscr, row_edit+' saved succesfully. Press any key to continue')
        except ValueError:
            status_bar(stdscr, 'Error, any key to continue. Saves gz12 graphs. Type : bool')
    
    elif row_edit == 'ini_layer_spacing':
        try:
            menu[row_edit] = float(new_setting)
            status_bar(stdscr, row_edit+' saved succesfully. Press any key to continue')
        except ValueError:
            status_bar(stdscr, 'Error, any key to continue. See docs. Type : int')

    elif row_edit == 'gb_type':
        try:
            menu[row_edit] = int(new_setting)
            status_bar(stdscr, row_edit+' saved succesfully. Press any key to continue')
        except ValueError:
            status_bar(stdscr, 'Error, any key to continue. See docs. Type : int')

    elif row_edit == 'gb_ends':
        try:
            menu[row_edit] = int(new_setting)
            status_bar(stdscr, row_edit+' saved succesfully. Press any key to continue')
        except ValueError:
            status_bar(stdscr, 'Error, any key to continue. See docs. Type : int')
    
    elif row_edit == 'atoms_per_monomer':
        try:
            menu[row_edit] = int(new_setting)
            status_bar(stdscr, row_edit+' saved succesfully. Press any key to continue')
        except ValueError:
            status_bar(stdscr, 'Error, any key to continue. See docs. Type : int')

    elif row_edit == 'number_of_monomer':
        try:
            menu[row_edit] = int(new_setting)
            status_bar(stdscr, row_edit+' saved succesfully. Press any key to continue')
        except ValueError:
            status_bar(stdscr, 'Error, any key to continue. For all chains. Type : int')
 
    elif row_edit == 'number_of_chains':
        try:
            menu[row_edit] = int(new_setting)
            status_bar(stdscr, row_edit+' saved succesfully. Press any key to continue')
        except ValueError:
            status_bar(stdscr, 'Error, any key to continue. For the whole simulation box. Type : int')

    elif row_edit == 'file_pattern':
        try:
            menu[row_edit] = new_setting.decode("utf-8")
            status_bar(stdscr, row_edit+' saved succesfully. Press any key to continue')
        except ValueError:
            status_bar(stdscr, 'Error, any key to continue. Should contain a *. Type : str')
 
 ################################################################################################

    stdscr.getch()        

def main(stdscr):
    # turn off cursor blinking
    curses.curs_set(0)
    
    # color scheme for selected row
    ## update color and references
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_RED)
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_WHITE)
    
    # specify the current selected row
    current_row = 0

    # print the menu
    print_menu(stdscr, current_row)
    status_bar(stdscr, "Arrow keys to move, Enter to edit and Enter again to confirm. Reference is called on type error.")

    while 1: ## perhaps a bit strong
    
        key = stdscr.getch()
        
        if ( key == curses.KEY_UP or key == ord('k') ) and current_row > 0:
            current_row -= 1
        elif ( key == curses.KEY_DOWN or key == ord('j') ) and current_row < len(menu)-1:
            current_row += 1

        elif ( key == curses.KEY_UP or key == ord('k') ) and current_row == 0:
            current_row = len(menu) - 1
        elif ( key == curses.KEY_DOWN or key == ord('j') ) and current_row == len(menu)-1:
            current_row = 0

        elif key == curses.KEY_ENTER or key in [10, 13]:
            # if user selected last row, exit the program
            if current_row == len(menu)-2:
                return True
            elif current_row == len(menu)-1:
                return False
            else:
               edit_options(stdscr, current_row)

        print_menu(stdscr, current_row)
        status_bar(stdscr, "Arrow keys to move, Enter to edit and Enter again to confirm. Reference is called on type error.")


def interface(menu_):

    global menu ## Not clean in Python but often seen in other languages. Would be to change
    
    menu = menu_
    menu.update(OrderedDict( [
        ('Run', 'Starts op script') ,
        ('Quit', 'Quits the script now')
        ] ) )
    
    run_flag = curses.wrapper(main)

    del menu['Run'] ; del menu['Quit']
    
    return run_flag, menu
    
