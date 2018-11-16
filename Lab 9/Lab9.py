#===============================================================================
# Lab 9  COMPSCI 1026 UWO
# November 16, 2018
# this exercise, you will write a program that makes use of two dictionaries. The program
# should read the data in rawdata.txt into a dictionary whose keys are country names and whose
# values are per capita incomes. Also create another dictionary whose keys are letters A‐ Z and
# whose values are sets of country names. Convert the country names to all uppercase for both
# dictionaries.
# Your program should prompt the user to enter an initial or a country names and then print the
# corresponding values.
# * If the user enters a string with only one letter (like A), the program should print all the
# countries that begin with that letter,
# * If the user enters a string that contains more than one letter, print the corresponding
# value for that country if it exists or print “Does not exist” if invalid.
# * Stop when the user enters quit.
#===============================================================================

rawdataFile = open("rawdata.txt", encoding='utf‐8', errors='ignore')
countriesDict = dict()
pk = 0
country = ""
population = 0
counter = 0
truncatedCountry = ""
matches = []

#populate countries
for i in rawdataFile:
    pk = i.rstrip().split(":")[0]
    country = i.rstrip().split(":")[1]
    population = i.rstrip().split(":")[2]
    countriesDict[country] = population
    

userSearch = input("Enter one or two characters of the countries name: ")

searchLength = len(userSearch)

for i in countriesDict:
    truncatedCountry = ""
    counter = 0
    while counter < searchLength:
        truncatedCountry += i[counter].lower()
        counter += 1
    if userSearch.lower() == truncatedCountry:
        matches.append([i,countriesDict[i]])
    
    
for i in matches:
    print("Country: " + i[0])
    print("Population: "+ i[1] )
    print("")