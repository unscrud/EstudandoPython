def is_triangle(a, b, c):
    case1 = a <= b+c
    case2 = b <= a+c
    case3 = c <= a+b

    if case1 and case2 and case3:
        print("Yes")
    else:
        print("No")


def take_user_input():
    a = int(input("type a "))
    b = int(input("type b "))
    c = int(input("type c "))
    is_triangle(a, b, c)


take_user_input()
