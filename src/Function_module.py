# A function  to calculate and store the total increase in population for each country between 1960 and
# 2020. Determine which country had the greatest total increase in population between
# 1960 and 2020
def population_increase(data, pop_increase):

    for c in data:
        start_pop = float(c[1])
        end_pop = float(c[61])
        diff_pop = end_pop - start_pop
        print(c[0], len(c))

        print(c[0], diff_pop)
        pop_increase.append((c[0], diff_pop))

    print(pop_increase)

    mvalue = pop_increase[0]

    for value in pop_increase[1:]:
        if mvalue[1] < value[1]:
            mvalue = value
    print("The country that had the greatest total increase is: ", mvalue)
    return mvalue


# A function to calculate and store the percentage increase in population for each country
# Between 1960 and 2020. Determine which country had the greatest percentage increase in
# Population between 1960 and 2020.
def percentage_increase(data, per_increase):

    for x in data:
        percentage = (float(x[61]) - float(x[1])) / float(x[1]) * 100
        per_increase.append((x[0], percentage))
    print(per_increase)

    perValue = per_increase[0]

    for y in per_increase[1:]:
        if perValue[1] > y[1]:
            perValue = y
    print("The country that had the greatest percentage increase is: ", perValue)
    return perValue


# A function to calculate and store the population density for the 10 most populated
# Countries in 1990 by find the 10 most populated countries in 1990 then dividing them by
# The area of each country.


def population_density_1990(data, pop_density, pop_list, top_ten):

    for i in range(10):
        maxPop = int(data[0][31])
        name = data[0][0]
        for j in range(1, len(data)):
            if data[j][0] == "High-income":
                continue
            pop = int(data[j][31])
            if maxPop < pop:
                if pop not in pop_list:
                    maxPop = pop
                    name = data[j][0]

        top_ten.append((name, maxPop))
        pop_list.append(maxPop)
    for f in top_ten:
        print(f[0], format(f[1], ","))
    country_area = [
        3705407,
        1269345,
        1711149,
        3796742,
        5070420,
        735358,
        3287956,
        6601670,
        145937,
        340509,
    ]
    for g in country_area:
        country_density = round((f[1] / g), 2)
        pop_density.append(country_density)
    print(
        "The population density for the top ten countries(stated above) in the year 1990 are as follows: ",
        pop_density,
    )


# A function to calculate and store the population density for the 10 most populated
# Countries in 2000 by find the 10 most populated countries in 2000 then dividing them by
# The area of each country.


def population_density_2000(data, pop_density2, pop_list2, top_ten2):

    for k in range(10):
        maxPop = int(data[0][41])
        name = data[0][0]
        for m in range(1, len(data)):
            if data[m][0] == "High-income":
                continue
            pop = int(data[m][41])
            if maxPop < pop:
                if pop not in pop_list2:
                    maxPop = pop
                    name = data[m][0]

        top_ten2.append((name, maxPop))
        pop_list2.append(maxPop)
    for q in top_ten2:
        print(q[0], format(q[1], ","))
    country_area = [
        3705407,
        1269345,
        1711149,
        5070420,
        3796742,
        735358,
        3287956,
        6601670,
        340509,
        57321,
    ]
    for n in country_area:
        country_density = round((q[1] / n), 2)
        pop_density2.append(country_density)
    print(
        "The population density for the top ten countries (stated above) in the year 2000 are as follows: ",
        pop_density2,
    )


# A function to determine the countries that had a top ten population in both 1990 and 2000
def top_ten_1990_2000(top_ten, top_ten2, pop_density3, top_ten3):
    for o in top_ten:
        for r in top_ten2:
            if o[0] == r[0]:
                if o[0] not in top_ten3:
                    top_ten3.append(o[0])
    print(top_ten3)


# A function to determine which countries had the biggest change in population density over
# The ten year span and the average change in population density for these countries during
# This decade
def biggest_population_density(
    pop_density3, top_ten, top_ten2, top_ten3, pop_density2, pop_density
):
    for i in range(10):
        if top_ten[i][0] in [name_country[0] for name_country in top_ten2]:
            den_diff = round((pop_density2[i] - pop_density[i]), 2)
            pop_density3.append((top_ten[i][0], den_diff))
    pop_density3.sort(key=lambda x: x[1], reverse=True)
    total = 0
    for z in range(0, len(pop_density3)):
        total += pop_density3[z][1]
    average_change_pop_density = round((total / len(pop_density3)), 2)
    print(
        "The countries that had the biggest change in population density over the 10-year span are as follows: ",
        pop_density3,
    )
    print(
        "The average change in population density for the 10-year span is as follows: ",
        average_change_pop_density,
    )
    return average_change_pop_density


# A Function with parameters that write a nicely formatted report to a file named formatted_report.
def report(
    mvalue,
    perValue,
    pop_density,
    pop_density2,
    pop_density3,
    average_change_pop_density,
    top_ten3,
):
    formatted_report = open("formatted_report_HK.txt", "w")
    formatted_report.write(
        "The country that had the greatest total increase is: " + str(mvalue) + "\n"
    )
    formatted_report.write(
        "The country that had the greatest percentage increase is: "
        + str(perValue)
        + "\n"
    )
    formatted_report.write(
        "The population density for the top ten countries in the year 1990 are as follows: "
        + str(pop_density)
        + "\n"
    )
    formatted_report.write(
        "The population density for the top ten countries in the year 2000 are as follows: "
        + str(pop_density2)
        + "\n"
    )
    formatted_report.write(
        "The countries that made the list for 1990 and 2000 are as follows: "
        + str(top_ten3)
        + "\n"
    )
    formatted_report.write(
        "The countries that had the biggest change in population density over the 10-year span are as follows: "
        + str(pop_density3)
        + "\n"
    )
    formatted_report.write(
        "The average change in population density for the 10-year span is as follows: "
        + str(average_change_pop_density)
        + "\n"
    )
