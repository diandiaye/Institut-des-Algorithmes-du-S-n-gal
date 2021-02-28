
def print_options():
    print("Options:")
    print(" 'p' print options")
    print(" 'c' convert from celsius")
    print(" 'b' Print n")
    print(" 'f' convert from fahrenheit")
    print(" 'q' quit the program")
 
def celsius_to_fahrenheit(c_temp):
    return 9.0 / 5.0 * c_temp + 32
 
def fahrenheit_to_celsius(f_temp):
    return (f_temp - 32.0) * 5.0 / 9.0
def boucle(n):
    for i in range(n):
        print(i)
choice = "p"
while choice != "q":
    if choice == "c":
        temp = input("Celsius temperature: ")
        print("Fahrenheit:", celsius_to_fahrenheit(temp))
    elif choice == "f":
        temp = input("Fahrenheit temperature: ")
        print("Celsius:", fahrenheit_to_celsius(temp))
    elif choice == "b":
        n = int(input("Choose n: "))
        print("Numbers:", boucle(n))
    elif choice != "q":
        print_options()
    choice = input("option: ")
