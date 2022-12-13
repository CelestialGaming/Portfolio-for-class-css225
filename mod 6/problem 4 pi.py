import math

r = int(input("Enter radius in metres (m) : ")) # I think it is possible to do inches or other measures but it seems meter is the default since when I used an external calculator to check my work, it didn't allign when using inches, so I switched to metre and it worked.
a = math.pi*math.pow(r,2) #Formula
int("Your radius", r, "m is calculated to Area. \nArea is = ", a, "m^2") #output