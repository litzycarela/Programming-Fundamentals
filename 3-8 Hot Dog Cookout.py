# Litzy Gabriella Carela    Sep 14, 2021
# Hot Dog Cookout Calculator V1.0,  Pgm 3-8
# Purpose: To find out if the user is an infant, child, teenager, or adult.

# Input(s):
# - People at Cookout
# - Hotdogs per Person

# Output(s):
# - Minimum Hotdogs Needed
# - Minimum Hotdog Buns Needed
# - Leftover Hot Dogs (lo_hd)
# - Leftover Hot Dog Buns (lo_hdb)

# Named Constants

HD_PACK = 10 # Stands for hotdogs per pack
HDB_PACK = 8 # Stands for hot dog buns per pack

# Gives a welcome message!
print("Hi there! The purpose of this program is too determine the minimum amount of Hot Dogs and Hot Dog Buns needed for your cookout (and how much will be let over).")

# User Input Below
people = int(input("Please enter the number of people attending your cookout: "))
hd_each = int(input("Please enter the number of hotdogs given to each person: ")) #hd_each is hotdogs per person

# Calculations
# - This is to find the minimum number of hot dogs per person
hd_minimum = people * hd_each 
# Now we'll see how many hot dog and bun packs we'll need 
hd_pkg = hd_minimum // HD_PACK
hdb_pkg = hd_minimum // HDB_PACK
# - Next we are going to see how many hotdog and bun packs we'll need to add to our total by looking for the remainder
needed_hd = hd_minimum % HD_PACK
needed_hdb = hd_minimum % HDB_PACK
lo_hd = 0 if needed_hd == 0 else HD_PACK - needed_hd
lo_hdb = 0 if needed_hdb == 0 else HDB_PACK - needed_hdb

# This is for adding extra packages
if needed_hd > 0:
    hd_pkg += 1
if needed_hdb > 0:
    hdb_pkg += 1

#Output Message
print(f'{hdb_pkg} packages of hot dog buns are required.')
print(f'{hd_pkg} packages of hot dogs are required.')
print(f'{lo_hdb} hot dog buns will be left over.')
print(f'{lo_hd} hot dogs will be left over.')