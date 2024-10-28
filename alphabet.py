# Create a list where everything is stored alphabetically from input.
a = []
while True:
    x = input("Enter a string: ")
    a.append(x)
    a.sort()
    print(a)