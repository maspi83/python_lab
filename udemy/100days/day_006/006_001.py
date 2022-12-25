def echo_ahoj():
    print ("Ahoj")

def echo_debil():
    print("Debil")

def echo_spolu():
    echo_ahoj()
    echo_debil()

number = 3
while number > 0:
    echo_spolu()
    number -= 1
    print (number)

while 1 > 0:
    echo_spolu()