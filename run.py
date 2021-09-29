import fileB

whatever = True

def thefunc():
    print("text now checker by @hani_j85")

while whatever == True:

    print("""
        1-mail access checker please run this first
        2-text now checker
    """)

    choice = input("Choice: ")

    if choice == "1":
        fileB.my_func()
        execfile('mailaccesschecker.py')


    elif choice == "2":
                fileB.my_func()
        execfile('textnowchecker.py')





    else:
        print("... again")