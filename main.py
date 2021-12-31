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
#   3. Each person receives only 1 gift
#
# A list of which families give a gift to which persons is outputted as a CSV 
# file ("new_givers.csv").
################################################################################
# Written by: Christopher Porco
################################################################################

import csv
import random

# Parses "families.csv" and adds it to a dictionary, and creates a list of all 
# persons (giftees)
def parseFamilies():
    families = dict()
    persons = list()

    with open('families.csv', newline = '') as families_csv:
        reader = csv.reader(families_csv, delimiter = ',', quotechar = '|')
        for row in reader:
            # Takes a row of CSV (as singleton string array), strips surrounding
            # whitespace, and splits into multiple strings 
            family = ','.join(row).strip().split(',')
            families[family[0]] = family[1:]
            for person in family[1:]:
                persons.append((person + " " + family[0]))

    return (families, persons)

# Parses "prev_givers.csv" and adds it to a dictionary
def parsePrevGivers():
    prev_givers = dict()

    with open('prev_givers.csv', newline = '') as prevGivers:
        reader = csv.reader(prevGivers, delimiter = ',', quotechar = '|')
        for row in reader:
            givers = ','.join(row).strip().split(',')
            prev_givers[givers[0]] = givers[1:]

    return prev_givers

# Creates a dictionary of each family (key) and a list of people to give a gift 
# to (value)
def assignGivers(families, prev_givers, unused_giftees):
    givers = dict()

    for giver in families:
        # Find list of possible giftees for 'giver' family
        possible_giftees = list()
        for family in families:
            # Satisfies constraint 1
            if (family != giver):
                for member in families[family]:
                    # Satisfies constraints 2 and 3
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

# Writes dictionary of families and giftees to a CSV file
def outputGivers(givers):
    with open('new_givers.csv', 'w', newline = '') as newGivers:
        writer = csv.writer(newGivers, delimiter = ',', quotechar = '|', 
                            quoting = csv.QUOTE_MINIMAL)
        for giver in givers:
            row = list()
            row.append(giver)
            for giftee in givers[giver]:
                row.append(giftee)
            writer.writerow(row)

def main():
    result = parseFamilies()
    families = result[0]
    giftees = result[1]
    prev_givers = parsePrevGivers()
    givers = assignGivers(families, prev_givers, giftees)
    outputGivers(givers)
    print("\nThe following is the new list of families and giftees: ")
    print(givers)

if __name__ == '__main__':
    main()