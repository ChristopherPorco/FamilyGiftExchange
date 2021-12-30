################################################################################
# Gift Exchange Script
################################################################################
# Given a dictionary of families ("families.csv"), this script assigns to each 
# family persons from another family to give a gift to, according to the 
# following constraints:
#
#   1. No person in a given family can give a gift to another member of the 
#      same family
#   2. No person can give a gift to the same person they gave a gift to in 
#      the previous year (as outlined in "prev_givers.csv")
#
# A list of which families give a gift to which persons is outputted as a CSV 
# file ("new_givers.csv").
################################################################################
# Written by: Christopher Porco
################################################################################

import random

def transferCSV():
    persons = dict()
    return persons

def assignGivers(persons):
    givers = dict()
    return givers

def outputGivers(givers):
    print("The givers have been outputted to a CSV")

def main():
    persons = transferCSV()
    givers = assignGivers(persons)
    outputGivers(givers)

if __name__ == '__main__':
    main()