

n = int(input("Please input a number to check if it's within 1-10: "))
def test_range(n):
    if n in range(1,10):
        print( " %s is in the range"%str(n))
    else :
        print("The number is outside the given range.")
test_range(n)