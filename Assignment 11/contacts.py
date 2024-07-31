# Program to implement a simple contact manager
# Fulufhelo Mulaudzi
# 08 May 2024


from math import floor


def path_exists(file_path):
    """This function checks whether a function exists or not"""
    import os.path
    if os.path.isfile(file_path):
        return True
    else:
        return False


def read_contacts(file_path):
    """This function reads the contents of a given file. It then lists the contents in a list and returns the list"""
    contacts = []
    f = open(file_path, "r")
    file = f.readlines()
    f.close()
    for line in file:
        line = line.replace("\n", "")
        line = line.split(",")
        contacts.append(line)
    return contacts


def add_contact(file_path, name, phone, email):
    """This function adds a new contact to a file. If the contact already exists then no new contact is added"""
    contents = read_contacts(file_path)
    for line in contents:
        if name in line[0]:
            print("Contact already exists.")
            return ""
    else:
        f = open(file_path, "a")
        person = f"{name},{phone},{email}\n"
        f.write(person)
        f.close()
        print("Contact added successfully.")
        return ""


def custom_sort(contacts):
    """This function sorts the given list of contacts alphabetically by the names of the contacts"""
    # The lambda function allow the contacts to be sorted by each index 0 of each list element which contains the names
    contacts.sort(key=lambda c: c[0])
    return contacts


def wildcard(pattern, word):
    """This function takes two arguments: a pattern and a word and then checks
        whether they are a match or not"""

    # First base case: checks if both pattern and word are empty
    if not word and not pattern:
        return True

    # Second base case: checks if one is empty and the other is not
    if not word or not pattern:
        return False

    # Third base case: checks if word is empty and pattern is '*'
    if not word and pattern == '*':
        return True

    # This section makes use of recursion to remove the first char and move on to the next if conditions are satisfied

    # This if checks if it is '*' and then compares the length of the word and pattern
    if pattern[0] == '*':

        if len(word) > 1 and len(pattern) > 1:
            # If second chars of both are equal, remove the first chars
            if pattern[1] == word[1]:
                return wildcard(pattern[1:], word[1:])
            elif pattern[1] == word[0]:
                return wildcard(pattern[1:], word)

        # If the lengths are equal then the first chars are removed and program continues
        if len(word) == len(pattern):
            return wildcard(pattern[1:], word[1:])

        # If word is less than pattern then the first char of pattern is removed
        elif len(word) < len(pattern):
            return wildcard(pattern[1:], word)

        # If the previous conditions are false, the first char of the word is removed until one condition is true
        else:
            return wildcard(pattern, word[1:])

    # This if checks if it is '?' and since it can be any char, it moves on to the next char
    if pattern[0] == '?':
        return wildcard(pattern[1:], word[1:])

    # This if checks if the chars are the same and then moves on to the next char
    elif word[0] == pattern[0]:
        return wildcard(pattern[1:], word[1:])
    return False


def ternary_search(data, item, left, right):
    """This function uses the ternary search algorithm in a recursive form to search
     for an item and returns its index if found"""
    if left > right:
        return -1

    # These calculations are for finding the two middle values
    m1 = left + floor((right - left) / 3)
    m2 = right - floor((right - left) / 3)

    if item in data[m1]:
        return m1
    if item in data[m2]:
        return m2

    if item < data[m1]:
        return ternary_search(data, item, left, m1-1)
    elif item > data[m2]:
        return ternary_search(data, item, m2+2, right)
    else:
        return ternary_search(data, item, m1+1, m2-1)


def search_contact(file_path, query):
    """This function searches takes a query and searches for a contact that matches the query.
    If a matching contact is found the function returns the contact and their information"""
    file = read_contacts(file_path)
    file = custom_sort(file)
    result = []

    # Checks if the query is an email
    if "@" in query:
        emails = []
        for line in file:
            emails.append(line[2])
        emails_result = ternary_search(emails, query, 0, len(emails)-1)
        if emails_result > -1:
            result.append(file[emails_result])

    # Checks if the query is a phone number
    elif query.isnumeric():
        numbers = []
        for line in file:
            numbers.append(line[1])
        numbers_result = ternary_search(numbers, query, 0, len(numbers)-1)
        if numbers_result > -1:
            result.append(file[numbers_result])

    # Checks if query is a wildcard
    elif "*" in query or "?" in query:
        match = []
        for line in file:
            # Checks wildcard against the names and then appends to list if they match
            if wildcard(query, line[0]):
                match.append(line)
        result.extend(match)
    # Last case checks if query is a name
    else:
        names = []
        for line in file:
            names.append(line[0])
        names_result = ternary_search(names, query, 0, len(names)-1)
        if names_result > -1:
            result.append(file[names_result])
    if result:
        print("Found contact(s):")
        grid_printer(result)
        return ""
    else:
        print("No contact found.")
        return ""


def grid_printer(people):
    """This function is responsible for the table that the contacts are displayed in"""
    print("="*60)
    print("|", end=" ")
    print('{:<20} '.format("Name"), end='')
    print("|", end=" ")
    print('{:<15} '.format("Phone"), end='')
    print("|", end=" ")
    print('{:<25} '.format("Email"), end='')
    print("|")
    print("="*60)
    for person in people:
        print("|", end=" ")
        print('{:<20} '.format(person[0]), end='')
        print("|", end=" ")
        print('{:<15} '.format(person[1]), end='')
        print("|", end=" ")
        print('{:<25} '.format(person[2]), end='')
        print("|")
        print("-" * 60)


def list_contacts(file_path):
    """This function lists out all contacts in a file in alphabetical order"""
    file = read_contacts(file_path)
    file = custom_sort(file)
    print()
    print("List of contacts:")
    grid_printer(file)


def main():
    name = input("Enter the name for the contacts file:\n")
    filename = name + ".txt"
    go_on = True

    # If the file does not exist, it is created
    if not path_exists(filename):
        f = open(filename, "w")
        f.close()
        print(f"Contacts file '{filename}' created.")

    while go_on:
        print()
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. List Contacts")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter name: ")
            number = input("Enter phone number: ")
            email = input("Enter email: ")
            add_contact(filename, name.title(), number, email)

        elif choice == 2:
            response = input("Enter first name, last name, phone number, or email to search:\n")
            search_contact(filename, response)

        elif choice == 3:
            # List out contacts using list function
            list_contacts(filename)

        elif choice == 4:
            go_on = False
            print("Exiting program.")


if __name__ == '__main__':
    main()
