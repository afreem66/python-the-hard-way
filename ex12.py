print("how old are you?", end='  ')
age = input()
print("how tall are you?", end='  ')
height = float(input())
print("how much do you weigh?", end='  ')
weight = float(input())

print(f"so you are {age} years old, {height * 2.54} cm tall and weigh {weight / 2.2} kg")
