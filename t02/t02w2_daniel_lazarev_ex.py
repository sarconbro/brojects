# Namensdrucker
names = ["Anna", "Bob", "Charlie", "David", "Eva"]

def list_of_names(names):
    for name in names:
        if name == "Charlie":
            print(f'Hello, {name}! You are the best!')
            continue
        print(f'Hello, {name}!')

list_of_names(names)