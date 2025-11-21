# car.py
import random
from typing import Optional

# Sets out the performance characteristics of the F1 car, including the different levels of tire compound sand their effects on wear and fuel consumption
class Car:
    COMPOUNDS = {"soft": {"wear_min": 8.0, "wear_max": 15.0, "fuel_mod": 1.15}, "medium": {"wear_min": 7.0, "wear_max": 12.0, "fuel_mod": 1.00}, "hard": {"wear_min": 5.0, "wear_max": 10.0, "fuel_mod": 0.85}}

    def __init__(
        self,
        make: str,
        model: str,
        fuel_capacity: float,
        mpg: float,
        tire_compound: str = "medium",
        fuel_level: Optional[float] = None,
        tire_wear: float = 0.0,
        odometer: float = 0.0,
    ):
        self.make = make
        self.model = model
        self.fuel_capacity = float(fuel_capacity)
        self.mpg = float(mpg)
        self.tire_compound = self._validate_compound(tire_compound)

        if fuel_level is None:
            self.fuel_level = self.fuel_capacity
        else:
            self.fuel_level = max(0.0, min(float(fuel_level), self.fuel_capacity))

        # race state
        self.tire_wear = max(0.0, min(float(tire_wear), 100.0))
        self.odometer = float(odometer)

    def _validate_compound(self, compound: str) -> str:
        compound = compound.lower()
        if compound not in self.COMPOUNDS:
            return "medium"
        return compound

    # simulate a lap, using driver efficiency & tire compound to degrade fuel level, and tire compound to degrade tires
    def drive_lap(self, distance_miles: float, efficiency_modifier: float = 1.0):
        compound_stats = self.COMPOUNDS[self.tire_compound]

        # base fuel
        base_fuel = distance_miles / self.mpg
        fuel_needed = base_fuel * efficiency_modifier * compound_stats["fuel_mod"]

        # compound-based tire wear
        lap_wear = random.uniform(
            compound_stats["wear_min"], compound_stats["wear_max"]
        )

        if fuel_needed > self.fuel_level:
            # can't finish the lap — drive only as far as fuel allows
            actual_distance = (
                self.fuel_level
                / (efficiency_modifier * compound_stats["fuel_mod"])
            ) * self.mpg
            self.odometer += actual_distance
            self.fuel_level = 0.0
            self.tire_wear = min(100.0, self.tire_wear + lap_wear)
            return actual_distance, False
        else:
            # normal full lap
            self.fuel_level -= fuel_needed
            self.odometer += distance_miles
            self.tire_wear = min(100.0, self.tire_wear + lap_wear)
            return distance_miles, True

    def needs_pit_stop(self) -> bool:
        low_fuel = self.fuel_level < 0.15 * self.fuel_capacity # pit if under 15% remaining fuel
        worn_tires = self.tire_wear > 85.0 # maximum tire degradation is 15% so pit when tires more than 85% worn
        return low_fuel or worn_tires

    def refuel(self):
        self.fuel_level = self.fuel_capacity

    def change_tires(self):
        # keep the same compound, just reset wear
        self.tire_wear = 0.0

    def set_tire_compound(self, compound: str):
        self.tire_compound = self._validate_compound(compound)
        self.tire_wear = 0.0

    def get_status(self) -> str:
        return (
            f"Fuel: {self.fuel_level:.1f} / {self.fuel_capacity:.1f} gal "
            f"— Tire wear: {self.tire_wear:.1f}% "
            f"— Compound: {self.tire_compound.capitalize()} "
            f"— Odometer: {self.odometer:.1f} mi"
        )
