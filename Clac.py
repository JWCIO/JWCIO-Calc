print("Welcome to... Somewhere, I guess. Is this a void? I can't see. Well, please enter your numbers and operation.")
numo = float(input("Number 1?"))
numt = float(input("Number 2?"))
operat = input("Add, sub, mul, or div?").lower()
res = 0
cont=False

def add():
    global numo, numt, res, cont
    res = numo + numt
    print(res)
    cont= input("Continue? y/n").lower()
    if cont == "y":
        
        operat = input("Add, sub, mul, or div?").lower()
        numo = res
        numt = float(input("Number 2?"))
        if operat == "add":
            add()
        elif operat == "sub":
            sub()
        elif operat == "mul":
            mul()
        elif operat == "div":
            div()
        else:
            print("That's not a valid operation. Please restart the program and try again.")
    elif cont == "n":
        print("Goodbye!")
    else:
        print("Invalid input. Please enter y or n.")
def sub():
    global numo, numt
    res = numo - numt
    print(res)
    cont= input("Continue? y/n").lower()
    if cont == "y":
        
        operat = input("Add, sub, mul, or div?").lower()
        numo = res
        numt = float(input("Number 2?"))
        if operat == "add":
            add()
        elif operat == "sub":
            sub()
        elif operat == "mul":
            mul()
        elif operat == "div":
            div()
        else:
            print("That's not a valid operation. Please restart the program and try again.")
    elif cont == "n":
        print("Goodbye!")
    else:
        print("Invalid input. Please enter y or n.")
def mul():
    global numo, numt
    res = numo*numt
    print(res)
    cont= input("Continue? y/n").lower()
    if cont == "y":
        
        operat = input("Add, sub, mul, or div?").lower()
        numo = res
        numt = float(input("Number 2?"))
        if operat == "add":
            add()
        elif operat == "sub":
            sub()
        elif operat == "mul":
            mul()
        elif operat == "div":
            div()
        else:
            print("That's not a valid operation. Please restart the program and try again.")
    elif cont == "n":
        print("Goodbye!")
    else:
        print("Invalid input. Please enter y or n.")
def div():
    global numo, numt
    if numo == 0:
        spawn = 0
        for spawn in range(0,int(numt)):
            print("0")
            spawn = spawn + 1
        res = "Zero divided by anything is zero, so here's a bunch of zeros."
    elif numt == 0:
        spawn = 0
        for spawn in range(0,int(numo)):
            print("0")
            spawn = spawn + 1
        res = "You can't divide by zero, so here's a bunch of zeros."
    else:
        res = numo/numt
    print(res)
    cont= input("Continue? y/n").lower()
    if cont == "y":
        
        operat = input("Add, sub, mul, or div?").lower()
        numo = res
        numt = float(input("Number 2?"))
        if operat == "add":
            add()
        elif operat == "sub":
            sub()
        elif operat == "mul":
            mul()
        elif operat == "div":
            div()
        else:
            print("That's not a valid operation. Please restart the program and try again.")
    elif cont == "n":
        print("Goodbye!")
    else:
        print("Invalid input. Please enter y or n.")

    
if operat == "add":
    print(add())
elif operat == "sub":
    print(sub())
elif operat == "mul":
    print(mul())
elif operat == "div":
    print(div())
else:
    print("That's not a valid operation. Please restart the program and try again.")







































if res == 42.0:
    print("The answer to life, the universe, and everything.")
elif res == 69.0:
    print("Nice.")
elif res == 420.0:
    print("Blaze it.")
elif res == 7.0:
    print("Lucky number seven!")
elif res == 3.14:
    print("Pi!")
elif res == 1.6180339887:
    print("The golden ratio!")
elif res == 0.0:
    print("Zero, the additive identity.")
elif res == 13.0:
    print("Unlucky for some.")
elif res == 100.0:
    print("A perfect score!")
elif res == 666.0:
    print("The number of the beast!")
elif res == 2020.0:
    print("The year of the pandemic!")
elif res == 1776.0:
    print("The year of American independence!")
elif res == 1492.0:
    print("The year Columbus sailed the ocean blue!")
elif res == 1066.0:
    print("The year of the Norman Conquest!")
elif res == 2001.0:
    print("The year of the first Harry Potter book!")
elif res == 1984.0:
    print("The year of Orwell's dystopia!")
elif res == 1914.0:
    print("The year World War I began!")
elif res == 1945.0:
    print("The year World War II ended!")
elif res == -1.0:
    print("You have found Euler's identity! E^(iπ) + 1 = 0. Catch it if you can!")
elif res == 2004:
    print("The end of the curse of the Bambino!")
elif res == 2007:
    print("Rocktober! A shame it was cut short by Boston.")
elif res == 2016:
    print("The Cubs win the World Series for the first time in 108 years!")
elif res == 2137:
    print("The time of the great Polish meme!")
elif res == 11:
    print("Snake eyes! Double ones!")
elif res == "-0":
    print("How is that even possible? You found negative zero!")
elif res == ":D":
    print("A smiley face! You found happiness in math!")
elif res == "Null":
    print("You found null! The absence of value!")
elif res == "Infinity":
    print("You found infinity! The concept of endlessness!")
elif res == "Undefined":
    print("You found undefined! A value that does not exist!")
elif res == "Error":
    print("You found an error! Something went wrong!")
elif res == "NaN":
    print("You found NaN! Not a number!")
elif res == 404:
    print("You found 404! The error code for not found!")
elif res == 403:
    print("You found 403! The error code for forbidden!")
elif res == 500:
    print("You found 500! The error code for internal server error!")
elif res == 418:
    print("You found 418! The error code for I'm a teapot! Wait, what?")
elif res == 2048:
    print("You found 2048! The game where you combine tiles to reach 2048!")
elif res == 1234:
    print("You found 1234! A simple sequence of numbers! Hopefully not a password!")
elif res == 505:
    print("You found 505! The error code for HTTP version not supported! Also leet speak for 'SO5' or 'SOS'!")
elif res == "H4CK3R":
    print("Uh... you found 'H4CK3R'? Are you trying to hack me? Nice try, but I'm just a simple calculator program!")
elif res == "No":
    print("You found 'No'? Well, that's a negative response! Maybe try again with a positive attitude?")
elif res == "Yes":
    print("You found 'Yes'? That's a positive response! Keep up the good vibes!")
elif res == "Maybe":
    print("You found 'Maybe'? That's indecisive! Make up your mind!")
elif res == 41:
    print("AI? Leet speak for 'A1'? You found artificial intelligence in a calculator program!")
elif res == 1010101010:
    print("You found a binary sequence! In decimal, that's 682! Binary is the language of computers!")
elif res == 137:
    print("You found 137! The fine-structure constant, a fundamental physical constant characterizing the strength of the electromagnetic interaction between elementary charged particles!")
elif res == 73:
    print("You found 73! The 21st prime number! Also, in binary, it's a palindrome: 1001001!")
elif res == 2012:
    print("You found 2012! The year of the Mayan calendar's supposed apocalypse! Spoiler: it didn't happen!")
elif res == 1871:
    print("You found 1871! The year of the Great Chicago Fire! A significant event in American history! Also, the foundation of the National Association of Professional Baseball.")
elif res == 1876:
    print("You found 1876! The year Alexander Graham Bell was awarded the patent for the telephone! A revolutionary invention that changed communication forever! Also, the foundation of the National League of Professional Baseball Clubs and Colorado became a state.")
elif res == 1903:
    print("You found 1903! The year the Wright brothers made their first powered flight! A monumental achievement in aviation history! Also, the first Tour de France was held and the first World Series in baseball took place.")
elif res == 1818:
    print("Treadmills were invented in 1818 as a form of punishment for prisoners in British prisons. They were used to keep prisoners occupied and to generate power for grinding grain or pumping water.")
elif res == 714:
    print("Babe Ruth's Homerun record of 714 stood for 39 years until it was broken by Hank Aaron in 1974.")
elif res == 755:
    print("Hank Aaron's Homerun record of 755 stood for 33 years until it was broken by Barry Bonds in 2007.")
elif res == 762:
    print("Barry Bonds' Homerun record of 762 is still standing, but it is controversial due to allegations of performance-enhancing drug use.")
