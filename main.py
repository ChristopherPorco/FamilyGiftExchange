################################################################################
# Family Gift Exchange Script
################################################################################
# Given a dictionary of families ("families.csv"), this script assigns to each 
# family persons from another family to give a gift to, according to the 
# following constraints:
#
#   1. No person in a given family can give a gift to another member of the 
#      same family
#   2. No person can give a gift to the same person they gave a gift to in 
#      the previous year (as outlined in "prev_givers.csv")
#   3. Each person receives only 1 gift
#
# A list of which families give a gift to which persons is outputted as a CSV 
# file ("new_givers.csv").
#
# For more information about this script, see the associated "README.md" file.
################################################################################
# Written by: Christopher Porco
################################################################################

import csv
import random

# Reads a CSV file (filename) and returns a tuple containing (1) a dictionary 
# version of the CSV file and (2) a list of all values in the CSV file (with 
# key appended to the end of each value)
def readCSVToDict(filename):
    dictionary = dict()
    items = list()

    with open(filename, newline = '') as csv_file:
        reader = csv.reader(csv_file, delimiter = ',', quotechar = '|')
        for row in reader:
            entry = ','.join(row).strip().split(',')
            dictionary[entry[0]] = entry[1:]

            for item in entry[1:]:
                items.append((item + " " + entry[0]))
    return (dictionary, items)

# Writes a dictionary (dictionary) to a CSV file (filename)
def writeDictToCSV(filename, dictionary):
    with open(filename, 'w', newline = '') as new_file:
        writer = csv.writer(new_file, delimiter = ',', quotechar = '|', 
                            quoting = csv.QUOTE_MINIMAL)
        for key in dictionary:
            row = list()
            row.append(key)
            for item in dictionary[key]:
                row.append(item)
            writer.writerow(row)

# Returns the second element of a tuple
def getSecondElem(t):
    return t[1]

# Sorts a CSV file according to the number of elements in each row, from largest
# to smallest number of elements
def sortCSV(filename):
    result = readCSVToDict("families.csv")
    unsorted_dict = result[0]

    # Creates a list of two-element tuples containing (1) the original position
    # of a row in the original CSV file, and (2) the number of items in that row
    items = list()
    for key in unsorted_dict:
        new_item = (key, len(unsorted_dict[key]))
        items.append(new_item)

    items.sort(reverse = True, key = getSecondElem)

    sorted_dict = dict()
    for item in items:
        key = item[0]
        sorted_dict[key] = unsorted_dict[key]

    writeDictToCSV("families.csv", sorted_dict)

# Creates a dictionary of each family (key) and a list of people to give a gift 
# to (value)
def assignGivers(families, prev_givers, unused_giftees):
    givers = dict()
    for giver in families:
        # Find list of possible giftees for 'giver' family according to 
        # constraints
        possible_giftees = list()
        for family in families:
            if (family != giver):
                for member in families[family]:
                    fullname = member + " " + family
                    if ((member not in prev_givers[giver]) and 
                            (fullname in unused_giftees)):
                        possible_giftees.append(fullname)

        # Randomly pick from possible giftees
        giftees = list()
        num_giftees = len(families[giver])

        for i in range(num_giftees):
            new_giftee = random.randint(0, len(possible_giftees) - 1)
            giftees.append(possible_giftees[new_giftee])
            unused_giftees.remove(possible_giftees[new_giftee])
            possible_giftees.remove(possible_giftees[new_giftee])
        givers[giver] = giftees

    return givers

def main():
    sortCSV("families.csv")

    families_result = readCSVToDict("families.csv")
    families = families_result[0]
    giftees = families_result[1]

    prev_givers_result = readCSVToDict("prev_givers.csv")
    prev_givers = prev_givers_result[0]

    givers = assignGivers(families, prev_givers, giftees)
    writeDictToCSV("new_givers.csv", givers)

    print("\nThe following is the new list of families and giftees: ")
    print(givers)

if __name__ == '__main__':
    main()