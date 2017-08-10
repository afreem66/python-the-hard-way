# i = 0
# numbers = []
#
# while i < 6:
#     print(f"At the top i is {i}")
#     numbers.append(i)
#
#     i = i + 1
#     print("Numbers now: :", numbers)
#
#     print(f"At the bottom i is {i}")
#
# print("The numbers: ")
#
# for num in numbers:
#     print(num)

def print_numbers(number):
    i = 0
    numbers = []

    while i < number:
        print_status("top", i)
        numbers.append(i)

        i += 1
        print("Numbers now: :", numbers)

        print_status("bottom", i)

    print("The numbers: ")

    for num in numbers:
        print(num)

def print_status(num, position):
    print(f"At the {position} i is {num}")

print_numbers(20)
