# generate headings (eg: -----Heading-----)
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Display instructions
def instructions():
    statement_generator(statement="The Ultimate Factor Finder", decoration="-")

    print('''
 To use this program simply enter an integer between
 1 and 200. The program will show the factors of your 
 chosen integer.

 It will also tell you if your chosen number...
 - is a prime number (ie: it has two factors)
 - is a perfect square

 To exit the program, please type 'xxx'
    ''')


# Ask user for am integer between 1 and 200
def num_check(question):
    error = "please enter a number that is between 1 and 200 inclusive\n"
    while True:

        response = input(question).lower()
        if response == "xxx":
            return response

        try:
            # ask the user for a number
            response = int(response)

            # check that the number is between 1 and 200
            if 1 <= response <= 200:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main routine goes here

statement_generator(statement="The Ultimate Factor Finder", decoration="-")

# Display instructions if requested
want_instructions = input("\npress <enter> to read the instructions "
                          "or any key to continue")

if want_instructions == "":
    instructions()

print("program continues")

# Ask users for an Integer
while True:
    to_factor = num_check("To factor: ")
    print("You chose to factor", to_factor)

    if to_factor == "xxx":
        break

