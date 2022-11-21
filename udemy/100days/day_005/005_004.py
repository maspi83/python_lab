for count in range(1,101):
    if count % 3 == 0:
        if count % 5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif count % 5 == 0:
        print("Buzz")
    else:
        print(count)