class MathGame:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.completed = False

class LewisCarrollsGameOfLogic(MathGame):
    def __init__(self):
        super().__init__("Lewis Carroll's Game of Logic", "A puzzle game based on mathematical logic puzzles.")

class PascalsTriangle(MathGame):
    def __init__(self):
        super().__init__("Pascal's Triangle", "An interactive exploration of Pascal's Triangle.")

class Nim(MathGame):
    def __init__(self):
        super().__init__("Nim", "A strategic game based on the mathematical game of Nim.")

class TheCandyGame(MathGame):
    def __init__(self):
        super().__init__("The Candy Game", "A counting and probability game.")

# Instantiate game objects
game1 = LewisCarrollsGameOfLogic()
game2 = PascalsTriangle()
game3 = Nim()
game4 = TheCandyGame()

# Mid-point milestone completion
game1.completed = True
game2.completed = True
game3.completed = True
game4.completed = True

# Display goals and mid-point milestone
print("Goals:")
print(f"[{game1.name}]")
print(f"[{game2.name}]")
print(f"[{game3.name}]")
print(f"[{game4.name}]")
print("[Goals Achieved By Mid-point Milestone]")
