# Program to insert and remove trace statements
# Fulufhelo Mulaudzi
# 03 May 2024

def add_tracer(filename):
    """This function takes in a file name and adds trace statements to it"""

    # It initially reads file data and stores it in a variable
    f = open(filename, "r")
    data = f.readlines()
    f.close()

    # It then writes to the file with the trace statements added in
    file = open(filename, "w")
    file.write('"""DEBUG"""\n')
    for line in data:
        file.write(line)
        if line[0:3] == 'def':

            # This slices out the function name and puts it in the trace statement
            index = line.find("(")
            name = line[4:index]
            file.write(f'    """DEBUG""";print(\'{name}\')\n')
    file.close()


def remove_tracer(filename):
    """This function takes a file name and removes trace statements found in it."""

    # It initially reads file data and stores it in a variable
    f = open(filename, "r")
    data = f.readlines()
    f.close()

    # It then writes to the file with the trace statements removed from it
    file = open(filename, "w")
    del data[0]
    for line in data:
        if line[0:15] == '    """DEBUG"""':
            del line
            continue
        file.write(line)
    file.close()


def main():
    print("***** Program Trace Utility *****")
    user_file = input("Enter the name of the program file: ")

    f = open(user_file, "r")
    first = f.readline()
    f.close()

    # Checks whether the file has trace statements or not
    if first == '"""DEBUG"""\n':
        print("Program contains trace statements")
        remove_tracer(user_file)
        print("Removing...Done")
    else:
        add_tracer(user_file)
        print("Inserting...Done")


if __name__ == '__main__':
    main()
