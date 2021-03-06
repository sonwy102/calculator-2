"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code

#Repeat foreever with while loop
while True:
    #read input
    user_input = input("Enter your equation: ")
    #use split function
    tokens = user_input.split(' ')

    #if first token is 'q', then quit
    if tokens[0] == 'q': 
        break
    else:
        if tokens[0] == 'pow':
            print (power(float(tokens[1]), float(tokens[2])))

        elif tokens[0] == '+':
            print(add(float(tokens[1]), float(tokens[2])))

        elif tokens[0] == '-':
            print(subtract(float(tokens[1]), float(tokens[2])))

        elif tokens[0] == '*':
            print(multiply(float(tokens[1]), float(tokens[2])))
        
        elif tokens[0] == '/':
            print(divide(float(tokens[1]), float(tokens[2])))

        elif tokens[0] == 'square':
            print(square(float(tokens[1])))
        
        elif tokens[0] == 'cube':
            print(cube(float(tokens[1])))
        
        elif tokens[0] == 'mod' or tokens[0] == '%':
            print(mod(float(tokens[1]), float(tokens[2])))
        else:
            print('invalid input')
