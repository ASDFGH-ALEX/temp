'''
Author:Alex
Date:28-10-2024
Description:Write a menu-driven Python program that allows users to convert temperatures between Celsius and Fahrenheit. The program should repeatedly display a menu with three options:

    Convert Celsius to Fahrenheit
    Convert Fahrenheit to Celsius
    Exit the program
'''
while True:
    print(" 1. \tConvert celsius to fahrenheit")
    print("2. \tConvert fahrenheit to celsius")
    print("3. \tExit the program")
    scale=int(input("Enter your choice"))
    if scale  ==1:
        temperature_1 = int(input("Enter the temperature"))
        Fahrenheit = (9 / 5 * scale) + 32
        print("convert celsius to fahrenheit",Fahrenheit)
    elif scale ==2:
        temperature_1 = int(input("Enter the temperature"))
        celsius = (scale- 32) * 5 / 9
        print("Convert fahrenheit to celsius",celsius)






