value_a = "" #first band
value_b = "" #second band
value_c = "" #third band
value_d = "" #fourth band
value_e = "" #Fifth band
choice = ["4", "5"]
band = ""

#valid color for first and second band (and third band if 5-band)
color_int = [
    "black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "gray", "white",
]
#valid color for multiplier
color_mul = [
    "black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "gray", "white", "gold",
    "silver"
]
#valid color for tolerance
color_tol = [
    "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "gray", "gold",
    "silver"
]

#code for color resistor

def value_hunds():
    global value0 ## to declare local value into global
    if value_e == "black":
        value0 = "0"
    elif value_e == "brown":
        value0 = "100"
    elif value_e == "red":
        value0 = "200"
    elif value_e == "orange":
        value0 = "300"
    elif value_e == "yellow":
        value0 = "400"
    elif value_e == "green":
        value0 = "500"
    elif value_e == "blue":
        value0 = "600"
    elif value_e == "violet":
        value0 = "700"
    elif value_e == "grey" or value_a == "gray":
        value0 = "800"
    elif value_e == "white":
        value0 = "900"
    elif value_e not in color_int:
        print("Incorrect! Try again")

def value_tens():
    global value1 ## to declare local value into global
    if value_a == "black":
        value1 = "0"
    elif value_a == "brown":
        value1 = "10"
    elif value_a == "red":
        value1 = "20"
    elif value_a == "orange":
        value1 = "30"
    elif value_a == "yellow":
        value1 = "40"
    elif value_a == "green":
        value1 = "50"
    elif value_a == "blue":
        value1 = "60"
    elif value_a == "violet":
        value1 = "70"
    elif value_a == "grey" or value_a == "gray":
        value1 = "80"
    elif value_a == "white":
        value1 = "90"
    elif value_a not in color_int:
        print("Incorrect! Try again")

def value_ones():
    global value2 ## to declare local value into global
    if value_b == "black":
        value2 = "0"
    elif value_b == "brown":
        value2 = "1"
    elif value_b == "red":
        value2 = "2"
    elif value_b == "orange":
        value2 = "3"
    elif value_b == "yellow":
        value2 = "4"
    elif value_b == "green":
        value2 = "5"
    elif value_b == "blue":
        value2 = "6"
    elif value_b == "violet":
        value2 = "7"
    elif value_b == "grey" or value_b == "gray":
        value2 = "8"
    elif value_b == "white":
        value2 = "9"
    elif value_b not in color_int:
        print("Incorrect! Try again")

def value_mul():
    global value_mult, suffix ## to declare local value into global
    if value_c == "black":
        value_mult = "1"
        suffix = ""
    elif value_c == "brown":
        value_mult = "10"
        suffix = ""
    elif value_c == "red":
        value_mult = "100"
        suffix = ""
    elif value_c == "orange":
        value_mult = "1"
        suffix = "K"
    elif value_c == "yellow":
        value_mult = "10"
        suffix = "K"
    elif value_c == "green":
        value_mult = "100"
        suffix = "K"
    elif value_c == "blue":
        value_mult = "1"
        suffix = "M"
    elif value_c == "violet":
        value_mult = "10"
        suffix = "M"
    elif value_c == "grey" or value_c == "gray":
        value_mult = "0.1"
        suffix = "G"
    elif value_c == "white":
        value_mult = "1"
        suffix  = "G"
    elif value_c == "gold":
        value_mult = "0.1"
        suffix = ""
    elif value_c == "silver":
        value_mult = "0.01"
        suffix = ""
    elif value_c not in color_mul:
        print("Incorrect! Try again")

def value_tol():
    global value_tole ## to declare local value into global
    if value_d == "brown":
        value_tole = "1"
    elif value_d == "red":
        value_tole = "2"
    elif value_d == "orange":
        value_tole = "0.05"
    elif value_d == "yellow":
        value_tole = "0.02"
    elif value_d == "green":
        value_tole = "0.5"
    elif value_d == "blue":
        value_tole = "0.25"
    elif value_d == "violet":
        value_tole = "0.10"
    elif value_d == "grey" or value_d == "gray":
        value_tole = "0.05"
    elif value_d == "gold":
        value_tole = "5"
    elif value_d == "silver":
        value_tole = "10"
    elif value_d not in color_tol:
        print("Incorrect! Try again")
        value_tole = "error"

print("Welcome to resistor value look up checker v0.2")
while band not in choice:
    band = input("Is your resistor 4-band or 5-band? (type number): ")
    if band in choice:
        if band == "4":
            '''first value'''
            while value_a not in color_int:
                value_a = input("Type first color: ").lower()
                value_tens()
            '''second value'''
            while value_b not in color_int:
                value_b = input("Type second color: ").lower()
                value_ones()
            '''Multiplier'''
            while value_c not in color_mul:
                value_c = input("Type third color: ").lower()
                value_mul()
            '''tolerance'''
            while value_d not in color_tol:
                value_d = input("Type last color: ").lower()
                value_tol()

            sum_val = int(value1) + int(value2)
            total = int(sum_val) * float(value_mult)
            print("Your resistor value is " + str(total) + " " + suffix + "Ohms with tolerance of " + value_tole + "%")

        elif band == "5":
            '''first value'''
            while value_e not in color_int:
                value_e = input("Type first color: ").lower()
                value_hunds()
            '''second value'''
            while value_a not in color_int:
                value_a = input("Type second color: ").lower()
                value_tens()
            '''third value'''
            while value_b not in color_int:
                value_b = input("Type third color: ").lower()
                value_ones()
            '''Multiplier'''
            while value_c not in color_mul:
                value_c = input("Type fourth color: ").lower()
                value_mul()
            '''tolerance'''
            while value_d not in color_tol:
                value_d = input("Type last color: ").lower()
                value_tol()

            sum_val = int(value1) + int(value2) + int(value0)
            total = int(sum_val) * float(value_mult)
            rtotal = round(total)
            print("Your resistor value is " + str(rtotal) + " " + suffix + "Ohms with tolerance of " + value_tole + "%")
    else:
        print("Invalid choices! Please try again")




