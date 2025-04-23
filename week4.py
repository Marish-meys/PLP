def read_file(filename):
    """Reads the contents of a file and returns it."""
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except PermissionError:
        print("❌ Error: You don't have permission to read the file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred while reading: {e}")
    return None

def write_file(filename, content):
    """Writes modified content to a new file."""
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"✅ Successfully written to '{filename}'.")
    except PermissionError:
        print("❌ Error: You don't have permission to write to the file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred while writing: {e}")

def modify_content(content):
    """Example content modifier: converts text to uppercase."""
    return content.upper()

def main():
    read_filename = input("Enter the name of the file to read from: ")
    content = read_file(read_filename)

    if content is not None:
        print("\nOriginal Content:\n" + "-"*20)
        print(content)

        modified = modify_content(content)

        write_filename = input("\nEnter the name of the file to write to: ")
        write_file(write_filename, modified)

# Run the main program
main()
