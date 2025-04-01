def read_and_modify_file():
    try:
        # Ask the user for the input file name
        input_filename = input("Enter the name of the file to read: ")
        
        # Open and read the file
        with open(input_filename, "r") as infile:
            content = infile.read()
        
        # Modify the content (example: convert text to uppercase)
        modified_content = content.upper()
        
        # Create a new output file name
        output_filename = "modified_" + input_filename
        
        # Write the modified content to the new file
        with open(output_filename, "w") as outfile:
            outfile.write(modified_content)
        
        print(f"File successfully modified and saved as {output_filename}")
    
    except FileNotFoundError:
        print("Error: The specified file does not exist.")
    except PermissionError:
        print("Error: You do not have permission to read or write this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
read_and_modify_file()

