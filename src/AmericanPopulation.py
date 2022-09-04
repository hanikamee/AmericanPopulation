# This program will import a module, function module, which includes the calculations
# Of population increase, percentage increase, population density in 1990, population
# Density in 2000, the countries that had a population density and were in the top ten
# For 1990 and 2000, lastly, the countries that had the biggest change of population density
# From 1990 to 2000


# Import the module, function module, and giving it an alias. The module encompasses
# All the functions that were used to do the calculations.
import Function_module_HK as fm

# The main function opens the text file that has the original data, puts the data in a string
# After stripping the spaces, and reads the first line of the data. The function also contains
# Global variables
def main():
    textFile = open("population.txt", "r")

    # Reading the first line of the text file.
    textFile.readline()

    # Reading the next line of the text file
    line = textFile.readline()

    # Global variables that have empty lists
    data = []
    pop_increase = []
    per_increase = []
    pop_density = []
    pop_density2 = []
    pop_density3 = []
    top_ten = []
    top_ten2 = []
    top_ten3 = []
    pop_list = []
    pop_list2 = []
    average_change_pop_density = ""

    # A loop to strip the lines in the text file from spaces
    while line != "":
        fields = line.rstrip().split("\t")
        data.append(fields)
        line = textFile.readline()
    print(data)

    # Calling the population increase function from the function module
    mvalue = fm.population_increase(data, pop_increase)
    # Calling the percentage increase function from the function module
    perValue = fm.percentage_increase(data, per_increase)
    # Calling the 1990 population density function from the function module
    fm.population_density_1990(data, pop_density, pop_list, top_ten)
    # Calling the 2000 population density function from the function module
    fm.population_density_2000(data, pop_density2, pop_list2, top_ten2)
    # Calling the 1990 and 2000 population density function from the function module
    fm.top_ten_1990_2000(top_ten, top_ten2, pop_density3, top_ten3)
    # Calling the population increase function from the function module
    average_change_pop_density = fm.biggest_population_density(
        pop_density3, top_ten, top_ten2, top_ten3, pop_density2, pop_density
    )
    # Calling the report function from the function module.
    fm.report(
        mvalue,
        perValue,
        pop_density,
        pop_density2,
        pop_density3,
        average_change_pop_density,
        top_ten3,
    )


# Calling the main function
main()
