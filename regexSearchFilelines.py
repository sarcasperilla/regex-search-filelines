#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 11:05:28 2018

@author: michaelcasper
"""

# A program to search all files in a folder for a regular expression
# that is supplied by the user.

# The main call for this program is
# regex_search_function(folder, regular_expression)
# whwere folder is the folder to search, and regular_expression is a
# regex that the user wants to search for.
# Results are printed in the command window.

import os
import re


# Search file line for a regex match
def find_regex_match(regular_expression, line):
    """  """
    line_regex = re.compile(regular_expression)
    try:
        line_match = line_regex.search(line).group()
        return line_match
    except AttributeError:
        return None


# Convert .txt file to a list of lines
def file_to_lines(folder, filename):
    file = open('{0}/{1}'.format(folder, filename), 'r')
    filelines = file.readlines()
    return filelines


# Main function to call the entire program
def regex_search_filelines(folder, regular_expression):
    filelist = os.listdir(folder)
    for filename in filelist:
        filelines = file_to_lines(folder, filename)
        for line in filelines:
            line_match = find_regex_match(regular_expression, line)
            if line_match is None:
                continue
            else:
                print('Match from: {0}\n    {1}'.format(filename, line_match))
