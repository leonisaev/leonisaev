def data_types_vars_and_print_1():
    """
    int: 1, 3, 5, 9, -3, 0
    float: 1.0, 0.9, -0.7, 5.6, 8.0
    str: "hello", "0.2", '-98', 'True'
    bool: True, False

    """
    tim = "hello"
    myVariable = True

    myVariable = 3
    joe = myVariable

    var = "hello"
    print("hi")
    print(var)

def input_print_operators_2():
    print("What is your name?")
    name = input()
    print(name)

    #or

    name = input("What is your name: ")
    print(name)

    name = input("What is your name: ")
    print("Well hello there", name)

    """
    +  # addition
    -  # subtraction
    /  # division
    *  # multiplication
    **  # exponential
    //  # integer division (removes decimal portion)
    %  # modulus (gives remainder of division)
    """

    x = 5
    y = 6

    d = 12 % 5  # d is 2
    z = x + y  # z is 11
    w = x - y  # w is -1
    q = 5 * 6  # q is 30
    u = 10 / x  # u is 2.0
    p = 10 * 2.0  # p is 20.0
    t = x ** 3  # t is 125
    c = 28 // y  # c is 4

    x = (1 + 3) / 2  # x is 2.0
    y = 4 + 5 * 7  # y is 39

    newStr = "hello" + "tim"  # newStr is "hellotim"
    newStr2 = "python" * 3  # newStr2 is "pythonpythonpython"

    num1 = input("Pick a Number: ")
    num2 = input("Pick Another Number: ")

    SUM = num1 + num2

    print(SUM)

    #fix

    num1 = input("Pick a Number: ")
    num2 = input("Pick Another Number: ")

    SUM = int(num1) + int(num2)

    print(SUM)

    #bcase

    num1 = "43"
    num2 = int(num1)

def conditions_3():
    """
    <  # less than
    <=  # less than or equal to
    >  # greater than
    >=  # greater than or equal to
    ==  # equal to
    !=  # not equal to
    """

    x = 5
    y = 9

    x > y  # this is False
    y == x  # this is False
    x < y - 1  # this is True
    x + 1 != y  # this is True
    2.0 > 5  # this is False

    "hello" == "hello"  # this is True
    "tim" == "Tim"  # this is False
    "a" > "b"  # this is False
    "apple" < "tim"  # this is True

    "5" == 5  # this will return False

    # NOT ALLOWED
    2 > "hello"
    3.0 < "tim"
    # These result in errors

    check = "tim" == "joe"
    larger = 1 > 5
    bothSame = larger == check  # This will be comparing two boolean values together
    # if they are both the same we will get a True value

def if_elif_else_4():
    if 4 < 5:
        print("true")

    number = int(input("Please type a number: "))
    if number < 5:
        print("the number is less than 5")
    print("I always run")

    number = int(input("Please type a number: "))
    if number < 5:
        print("the number is less than 5")
    else:
        print("the number is NOT less than 5")

    number = int(input("Please type a number: "))

    if number < 5:
        print("the number is less than 5")
    elif number < 10:
        print("the number is greater than or 5 and less than 10")
    elif number < 15:
        print("the number is greater than or 10 and less than 15")
    else:
        print("the number is NOT less than 15")

    if number == 10:
        print("The number is 10")
    elif number == 15:
        print("The number is 15")