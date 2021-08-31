#FEW EXERCISES ON DATA

#1 population growth in Istambul 1927-2017

city_name = "Istambul, Turkey"
pop_1927 = 691000
pop_2017 = 15029231
pop_change = pop_2017 - pop_1927
percentage_gr = (pop_change / pop_1927) * 100

annual_gr = percentage_gr / (2017-1927)
print(annual_gr)

def population_growth(year_one, year_two, population_one, population_two):
  growth_rate = (((population_two - population_one)/population_one) * 100)/ (year_two - year_one)
  return growth_rate

set_one = population_growth(1927, 2017, pop_1927, pop_2017)
print(set_one)

set_two = population_growth(1950, 2000, 983000, 8831800)
print(set_two)

#wrapping up

report = "The number of population of ___ chaged a lot. "
print("In 1927, the population was " + str(pop_1927) + ", in 2017, it changed to " + str(pop_2017) + ". The overall change of population equals " + str(pop_change) + ". The annual growth rate of population is equal " + str(annual_gr))

#2 covid statistics comparison in Russia 2020 - 2021

print("covid statistics in Russia 2020 - 2021")
moscow_cases = 422000
moscow_deaths = 7766
rostov_cases = 124000
rostov_deaths = 5959

moscow_rate = moscow_deaths / moscow_cases
print(moscow_rate)
rostov_rate = rostov_deaths / rostov_cases
print(rostov_rate)

print("In Rostov, the death rates are higher than in Moscow.")

# IF YOU FOUND ANY MISTAKES IN MY CODE PLEASE FEEL FREE TO REACH ME !! SOFNAYD@GMAIL.COM
# I'M JUST A BEGINNER WITH SMOL EXPERIENCE HOPING TO BECOME A GENIOUS PROGRAMMER

# THANK YOU FOR CHECKING ON MY CODE <3 MEANS A LOT TO ME