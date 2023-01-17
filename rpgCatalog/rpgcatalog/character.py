class Character:

    def __init__(self, health: int = 1000, level: int = 1, alive: bool = True):
        """
        Character begin with 1000 health point and level 1.
        """
        self.health = health
        self.level = level
        self.alive = alive
