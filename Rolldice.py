import random
def roll_a_dice():
    return random.randint(1, 6)
result = roll_a_dice()
print("You rolled a", result)