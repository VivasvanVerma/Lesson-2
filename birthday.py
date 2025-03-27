print("Note: Please only enter the birth YEAR for the following questions.")
john = int(input("Hi John, When were you born? "))
steve = int(input("Hi Steve, When were you born? "))
tony = int(input("Hi Tony, When were you born? "))
paul = int(input("Hi Paul, When were you born? "))
noah = int(input("Hi Noah, When were you born? "))
print("John was born in ", john)
print("Steve was born in ", steve)
print("Tony was born in ", tony)
print("Paul was born in ", paul)
print("And finally, Noah was born in ", noah)
oldest = input("Would you like to know who is the oldest? ")
if oldest == "yes" or oldest == "Yes":
    print("Alright! I'll tell you!")
    if john <= steve and john <= tony and john <= paul and john <= noah:
        print("John is the oldest!")
    elif steve <= john and steve <= tony and steve <= paul and steve <= noah:
        print("Steve is the oldest!")
    elif tony <= john and tony <= steve and tony <= paul and tony <= noah:
        print("Tony is the oldest!")
    elif paul <= john and paul <= steve and paul <= tony and paul <= noah:
        print("Paul is the oldest!")
    else:
        print("Noah is the oldest!")
elif oldest == "no" or oldest == "No":
    print("Well, thats too bad. I'll tell you anyway.")
    if john <= steve and john <= tony and john <= paul and john <= noah:
        print("John is the oldest!")
    elif steve <= john and steve <= tony and steve <= paul and steve <= noah:
        print("Steve is the oldest!")
    elif tony <= john and tony <= steve and tony <= paul and tony <= noah:
        print("Tony is the oldest!")
    elif paul <= john and paul <= steve and paul <= tony and paul <= noah:
        print("Paul is the oldest!")
    else:
        print("Noah is the oldest!")