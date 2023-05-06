while True:
    try:
        # Prompt the user to enter a file name
        file_name = input("Enter the file name: ")

        # Attempt to open the file
        with open(file_name, 'r') as file:
            # Read the contents of the file
            contents = file.read()

            # Display the contents of the file
            print(contents)

        # Break out of the loop
        break

    except FileNotFoundError:
        print("File not found. Please enter a valid file name.")
    except IOError:
        print("Error reading file. Please check the file and try again.")
