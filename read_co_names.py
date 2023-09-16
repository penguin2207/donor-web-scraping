#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 21:10:27 2023

@author: jluciano
"""

def read_company_names_from_file(filename):
    with open(filename, "r") as file:
        company_names = [line.strip() for line in file.readlines()]
    return company_names

if __name__ == "__main__":
    filename = "companies.txt"  # Replace with the path to your text file
    company_names = read_company_names_from_file(filename)

    # Printing the array to verify the result
    print(company_names)
