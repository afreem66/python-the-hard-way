global_variable = "i am global"
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2} global: {global_variable}")

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2} global: {global_variable}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("i got nothin")

print_two('andrew', 'freeman')
print_two_again('danny', 'mackenzie')
print_one('andrewfreeman')
print_none()
