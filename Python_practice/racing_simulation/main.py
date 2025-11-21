# main.py
from driver import Driver
from car import Car
from race import Race   # <-- you were missing this
import sys

def main(argv):
    myCar = Car(
        make="Williams Racing",
        model="FW46",
        fuel_capacity=33,
        fuel_level=27,
        mpg=1.5,
        tire_wear=0,
        odometer=0,
        tire_compound="medium",
    )

    myDriver = Driver("Theo Symonds", "Williams Racing", 0.95)

    # laps=10, lap_distance=16.00 (whatever units you're using for miles)
    myRace = Race(myDriver, myCar, 35, 5.5)
    myRace.run()
    myRace.print_summary()

if __name__ == "__main__":
    main(sys.argv[1:])
