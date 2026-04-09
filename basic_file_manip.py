"""
File Management and Word Search Program

This program allows the user to:
1. Add text to a file
2. Display file content
3. Create a copy of a file
4. Search for a word (exact matches only)
5. Exit the program

Author: Greg Horvath
Date: 2026-04-07
Python version: 3.10+
"""

def menu():
    """
    Display the main menu to the user.
    
    Options:
        1 - Create a new text file
        2 - Display file content
        3 - Create a copy of a file
        4 - Search how many times a word appears in a file
        m - Show menu
        x - Exit
    """
    print("*" * 80)
    print("Option 1: Create a new text file.")
    print("Option 2: Display the content of a text file.")
    print("Option 3: Create a copy of a text file.")
    print("Option 4: Search how many times a word appears in a text file.")
    print("Option m: Show the menu")
    print("Option x: Exit")

menu ()

def search_file(file_name):
    """
    Check if a text file exists.

    Args:
        file_name (str): Name of the file without extension.

    Returns:
        True if the file exists, None if the file doesn't exist.
    """
    try:
        text_file = open(f"{file_name}.txt", 'r')
    except Exception as e:
        input(f"Error! No file found with name: {file_name}")
        return None
    else:
        text_file.close()
        return True
    
def is_word_char(c):
    """
    Check if a character is part of a word (letter or digit).

    Args:
        c (str or None): Single character to check.

    Returns:
        bool: True if c is a letter or digit, False otherwise.
    """
    if c is None:
        return False
    return (
        ('a' <= c <= 'z') or
        ('A' <= c <= 'Z') or
        ('0' <= c <= '9')
    )

option = input("Choose a menu option: ")

while option != "x":
    """
    Main program loop.

    This loop keeps running until the user selects 'x' to exit.
    Based on the user's choice, it executes:
    - File creation (option "1")
    - File display (option "2")
    - File copying (option "3")
    - Word search (option "4")
    - Menu display (option "m")
    """

    match option:
        case "1":
            """
            Option 1: Create a new text file.

            Steps:
            1. Ask for a file name.
            2. Open the file in append mode (creates it if it doesn't exist).
            3. Prompt the user for text input.
            4. Write the text to the file along with a sample line.
            5. Close the file.
            """
            file_name = input("Please enter the name of the file you'd like to use: ")
            text_file = open(f"{file_name}.txt", 'a')
            text_input = input("Please enter text you'd like to save into the file: ")
            text_file.write(text_input)
            text_file.write("\n")
            text_file.write(
                "This is a python sample text that contains the word python many times, "
                "to practice working with files in python.\n"
            )
            text_file.close()

        case "2":
            """
            Option 2: Display the content of a text file.

            Steps:
            1. Ask for the file name.
            2. Check if the file exists using search_file().
            3. Read the file line by line.
            4. Print each line with its number.
            """
            file_name = input("Please enter the name of the file you'd like to view: ")
            found = search_file(file_name)
            if found:
                with open(f"{file_name}.txt", 'r') as text_file:
                    line = text_file.readline()
                    counter = 1
                    while line:
                        print(f"{counter}: {line.rstrip()}")
                        line = text_file.readline()
                        counter += 1
            else:
                print(f"Couldn't find a file with name {file_name}")
                
        case "3":
            """
            Option 3: Create a copy of a text file.

            Steps:
            1. Ask for the file name.
            2. Check if the file exists using search_file().
            3. Open the original file for reading.
            4. Open a new file with '_copy' appended to the name in append mode.
            5. Copy each line from the original file to the copy.
            6. Close both files.
            """
            file_name = input("Please enter the name of the file you'd like to duplicate: ")
            found = search_file(file_name)
            if found:
                with open(f"{file_name}.txt", 'r') as original:
                    with open(f"{file_name}_copy.txt", 'a') as copy:
                        line = original.readline()
                        while line:
                            copy.write(line)
                            line = original.readline()
            else:
                print(f"Couldn't find a file with name {file_name}")
        
        case "4":
            """
            Option 4: Search for a word in a text file.

            Steps:
            1. Ask for the file name and check if it exists.
            2. Prompt the user for the word to search.
            3. Open the file with UTF-8 encoding, replacing invalid characters.
            4. Read the entire content of the file.
            5. Loop through each character, checking for exact matches of the word:
               - Ensure the word is not part of another word (letters or digits on either side).
            6. Count occurrences and display the result.
            """
            file_name = input("Please enter the name of the file you'd like to search in: ")
            found = search_file(file_name)

            if found:
                text_to_find = input("Please enter the word you'd like to find: ")
                count_occurrences = 0

                with open(f"{file_name}.txt", 'r', encoding='utf-8', errors='replace') as file:
                    text = file.read()

                    i = 0
                    while i < len(text):
                        match = True

                        # Try to match the word starting at position i
                        for j in range(len(text_to_find)):
                            if i + j >= len(text) or text[i + j] != text_to_find[j]:
                                match = False
                                break

                        if match:
                            # Character before the word
                            if i == 0:
                                before = None
                            else:
                                before = text[i - 1]

                            # Character after the word
                            if i + len(text_to_find) >= len(text):
                                after = None
                            else:
                                after = text[i + len(text_to_find)]

                            # Count only if it's a separate word
                            if not is_word_char(before) and not is_word_char(after):
                                count_occurrences += 1

                        i += 1

                print(f"The text '{text_to_find}' appears {count_occurrences} times in the file: {file_name}.txt")
            else:
                print(f"Couldn't find a file with name {file_name}")

        case "m":
            """Option m: Re-display the menu."""
            menu()

        case "x":
            """Option x: Exit the program loop."""
            break

        case _:
            """Handle invalid menu option input."""
            print("Option not available")

    print("+" * 80)
    option = input("Choose a menu option: ")
