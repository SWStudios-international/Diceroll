import random

history = []

while True:
    count = int(input("How many dice? (0 to quit) "))
    if count == 0:
        break

    rolls = []
    max_possible = 0

    for i in range(count):
        sides = int(input(f"How many sides on die #{i+1}? "))
        r = random.randint(1, sides)
        rolls.append(r)
        max_possible += sides

    total = sum(rolls)
    print("you rolled:", rolls, "for a total of", total)

    if total >= max_possible * 0.75:
        print("Calm it hot shot")
    else:
        print("WANT SOME WATER FOR THAT BURN OOOOOOH")

    history.append(rolls)

print("roll history:", history)
