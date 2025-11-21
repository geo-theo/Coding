# driver.py

# Sets out who is driving the car and their skill level for fuel/wear efficiency (float value between 0.0 and 1.0)
class Driver:
    def __init__(self, name: str, team: str, skill_level: float = 0.8):
        self.name = name
        self.team = team
        self.skill_level = max(0.0, min(skill_level, 1.0))

    def get_skill_modifier(self) -> float:
        """
        Returns an efficiency multiplier.
        Value < 1.0 = better efficiency (uses less fuel / less wear).
        We'll let a perfect driver (1.0) get 0.8, and a 0.0 driver get 1.0.
        """
        return 1.0 - (self.skill_level * 0.2) # subtract so that better driver uses less fuel/wear (better driver consumes 20% less)

    def __str__(self) -> str:
        return f"{self.name} ({self.team})"
