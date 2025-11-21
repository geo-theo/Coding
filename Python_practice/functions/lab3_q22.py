### 2.1.22 ###
######################################################################################################################
### Birthday problem. Compose a program with appropriate functions for studying the birthday problem (see 1.4.16). ###
######################################################################################################################
import stdio
import stdarray
import random
import sys

# define constant birthdays per year
DAYS_PER_YEAR = 365

# simulate one experiment (birthday.py)
def one_trial():
    birthdaysSeen = stdarray.create1D(DAYS_PER_YEAR, False)
    peopleCount = 0
    while True:
        peopleCount += 1
        birthday = random.randrange(DAYS_PER_YEAR)
        if birthdaysSeen[birthday]:
            return peopleCount
        birthdaysSeen[birthday] = True

# simulate n experiments and return the average number of people required (birthdays.py)
def average_trials(n):
    totalPeople = 0
    for i in range(n):
        totalPeople += one_trial()
    return float(totalPeople) / float(n)

# execute one function depending on argument given in command line: no arguments given is for one_trial, a given n argument is for average_trials
if len(sys.argv) == 1:
    # run once if no n given
    result = one_trial()
    stdio.writeln("Number of people (in single simulation) that must enter a room until two share a birthday: " + str(result))
else:
    # run n experiments and average
    n = int(sys.argv[1])
    avg = average_trials(n)
    stdio.writeln("Number of people (in " + str(n) + " simulations) that must enter a room until two share a birthday: " + str(avg))

