foods = []

for i in range(5):
    food = input("Enter your favorite food: ")
    foods.append(food)

print("Your Favorite Foods:")

for food in foods:
    print("-",food)