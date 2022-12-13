start = int(input("""1. Do you want to see numbers between 1-50?
. calculate numbers that are divisible by 3?
3. calculate numbers that are divisible by 5?
4. calculate numbers that are divisible by 5 and 3?"""))


if start == 1:
    for number in range(1,51):
        print(number)

elif start == 2:
    e = int(input("what is your number", ))

    if e % 3 == 0:
        print("divisible by 3!")
    else:
        print("not divisible by 3")

elif start == 3:
    a = int(input("what is your number", ))

    if a % 5 == 0:
        print("divisible by 5!")
    else:
        print("not divisible by 5")

elif start == 4:

    sports = int(input("what is your number", ))
    
    if sports % 3 == 0:
        print("divisible by 3!")
    elif sports % 5 == 0:
            print("divisible by 5!")
    else:
        print("not divisible by 5 or 3")
else:
    print("invalid input")


