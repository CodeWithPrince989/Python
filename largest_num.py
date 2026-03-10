a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))

if a > b and a > c:
    print("First Number Is greater")

elif b > a and b > c:
    print("Second Number Is greater")

elif c > a and c > b:
    print("Third Number Is greater")

else:
    print("Numbers may be equal")
