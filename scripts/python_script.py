import os

file_path = "scripts/dummy.log"  # Use relative path if the file is in the repository

def delete_file(file_path):
    try:
        print(f"Current working directory: {os.getcwd()}")
        print("Directory contents before deletion:")
        print(os.listdir())

        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"File '{file_path}' has been deleted successfully.")
        else:
            print(f"File '{file_path}' not found.")
        
        print("Directory contents after deletion:")
        print(os.listdir())
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    delete_file(file_path)
