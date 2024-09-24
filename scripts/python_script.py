import os
file_path = "/workspaces/actions/dummy.log"
def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"File '{file_path}' has been deleted successfully.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace 'your_file.txt' with the path to the file you want to delete
    delete_file(file_path)
