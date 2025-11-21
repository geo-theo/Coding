# race.py

from driver import Driver
from car import Car

# Race controls flow of race simulation
class Race:
    def __init__(self, driver: Driver, car: Car, laps: int, lap_distance: float):
        self.driver = driver
        self.car = car
        self.laps = int(laps)
        self.lap_distance = float(lap_distance)
        self.pit_stops = 0

    def run(self):
        print(f"Starting race for: {self.driver}")
        print(f"Initial car status — {self.car.get_status()}")
        print("-" * 50)

        for lap in range(1, self.laps + 1):
            # driver efficiency affects fuel/tire usage
            efficiency = self.driver.get_skill_modifier()
            miles_driven, finished = self.car.drive_lap(
                self.lap_distance, efficiency_modifier=efficiency
            )

            print(
                f"Lap {lap} complete — drove {miles_driven:.1f} mi — {self.car.get_status()}"
            )

            if not finished:
                print("Car ran out of fuel! Race ended early.")
                break

            # don't bother to pit after the last lap
            if lap != self.laps and self.car.needs_pit_stop():
                print("Pit stop needed! Refueling and changing tires...")
                self.car.refuel()
                self.car.change_tires()
                self.pit_stops += 1

        print("-" * 50)
        print("Race Complete!")

    def print_summary(self):
        print(f"Total distance: {self.car.odometer:.1f} miles")
        print(f"Pit stops: {self.pit_stops}")
        print(f"Fuel remaining: {self.car.fuel_level:.1f} gal")
