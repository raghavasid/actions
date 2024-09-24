import os

file_path = "dummy.log"  # Use relative path if the file is in the repository

def delete_file(file_path):
    try:
        print(f"Current working directory: {os.getcwd()}")
        os.remove(file_path)
        print(f"File '{file_path}' has been deleted successfully.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    delete_file(file_path)
