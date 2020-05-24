def check_fermat(a, b, c, n):
    result = a**n+b**n == c**n
    if(result and n > 2):
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn’t work.")


a = int(input("Type a ... "))
b = int(input("Type b ... "))
c = int(input("Type c ... "))
n = int(input("Type n ... "))
check_fermat(a, b, c, n)
