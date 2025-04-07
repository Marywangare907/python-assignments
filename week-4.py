def read_and_modify_file():
    try:
        input_filename = input("Enter the name of the file to read: ").strip()
        if not input_filename:
            print("Error: No filename provided. Please enter a valid filename.")
            return

        with open(input_filename, 'r') as infile:
            content = infile.readlines()

        modified_content = [f"{i + 1}: {line}" for i, line in enumerate(content)]

        output_filename = input("Enter the name of the file to write to: ").strip()
        if not output_filename:
            print("Error: No filename provided. Please enter a valid filename.")
            return

        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_content)

        print(f"File has been successfully modified and saved as '{output_filename}'.")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except IOError:
        print("Error: The file could not be read or written. Please check permissions and try again.")
