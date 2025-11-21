CSCI 151 Lab 5
Theo Symonds

########## driver.py ##########
This class represents the human driver and provides a skill level effect to determine how much fuel and tire wear happens each lap. This only matters for Race and not Car, since a different driver can affect a car differently when racing.

__init__:
Saves the driver’s name, team, and a skill_level between 0.0 and 1.0.

get_skill_modifier():
Returns a number the car can use to slightly increase or decrease fuel usage. The higher the skill the better the driver is for fuel and tire degradation efficiency, so we have to give them a lower multiplier (up to 20% better for the most skilled driver of 1.0)

__str__:
Returns a readable string like "Lewis Hamilton (Mercedes)". Used in Race.run() to give us context of who is driving.



########## car.py ##########
This class represents the F1 car parameters for performance and tracks its changing state during the race. Ideally you could change these parameters to reflect better/worse cars across teams.

Tire wear by compound (COMPOUNDS):
A dictionary that defines how each tire compound behaves, for wear minimum/maximum (random tire wear range per lap), and how the compound affects fuel usage (soft uses more fuel, hard uses less).

__init__:
Stores the car’s basic info: make, model, fuel tank size, mpg, odometer, and validates tire compound.

drive_lap():
Figure out how much fuel that lap needs, add tire wear, update the odometer, return whether the lap was actually finished.

need_pit_stop():
Check if we need to pit based on low fuel or high tire wear.

refuel():
Refuel back to full when below car fuel threshold.

change_tires():
resets tire wear to 0 but keeps the same compound.

set_tire_compound(compound):
changes the tire compound and resets wear.

get_status():
returns a string describing current fuel, tire wear, compound, and odometer.



########## race.py ##########
Controls the flow of the simulation (laps, pit stops, etc.)

__init__(...):
sets up the race with a driver, car, number of laps, and lap distance.

run():
runs the race lap by lap, including pit stops.

print_summary():
prints a short report at the end of the race.



########## main.py ##########
This is our test client.
Imports all previous files and constructs objects to run the simulations.

main(argv):
creates the objects (driver, car, race) and runs the simulation.