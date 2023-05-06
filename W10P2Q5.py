while True:
    try:
        filename = input("Enter the filename: ")
        with open(filename, "r") as file:
            # Check if the file is a text file by reading the first few bytes and checking for a UTF-8 BOM
            data = file.read(3)
            if data != '\ufeff':  # not a UTF-8 BOM
                raise ValueError("Invalid file format. Please enter a valid text file.")
            break
    except IOError:
        print("File not found. Please enter a valid filename.")
    except ValueError as e:
        print(e)
