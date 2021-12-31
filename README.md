# FamilyGiftExchange
## About
This Python script was written to solve a problem my family was having when picking out givers and giftees for our annual Christmas Eve gift exchange.

According to the following constraints, the program assigns to each family in "families.csv" a number of giftees based on the number of members in the giver family, with the giftees chosen at random based on a pool of possible giftees:
- No person in a given family can give a gift to another member of the same family
- No person can give a gift to the same person they gave a gift to in the previous year (as outlined in "prev_givers.csv")
- Each person receives only 1 gift

## How to Use
To use this program for yourself:
1. Clone or download this repository, making sure to keep "main.py," "families.csv," "prev_givers.csv," and "next_givers.csv" in the same directory
2. Following the format displayed in "families.csv," enter in the families and their members that are involved in the gift exchange
3. Following the format displayed in "prev_givers.csv," enter in the families and who they gave gifts to in the previous exchange. If there was not previous exchange, or if new families have joined the exchange from the previous year, simply enter in the family names and do not include any giftees
4. Run "main.py" as you would run any Python file
5. Open "next_givers.csv" for the new list of families and their giftees!
    
## Questions, Comments, or Suggestions
If you have any questions, comments, or suggestions about this script, please get in touch with me at porcochristopher@gmail.com or make a pull request.
