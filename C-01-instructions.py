# generate headings (eg: -----Heading-----)
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Display instructions
def instructions():
    statement_generator(statement="instructions", decoration="-")

    print('''
 To use this program simply enter an integer between
 1 and 200. The program will show the factors of your 
 chosen integer.
 
 It will also tell you if your chosen number...
 - is a prime number (ie: it has two factors)
 - is a perfect square
 
 To exit the program, please type 'xxx'
    ''')


# main routine goes here

# Display instructions if requested
want_instructions = input("press <enter> to read the instructions "
                          "or any key to continue")

if want_instructions == "":
    instructions()

print("program continues")