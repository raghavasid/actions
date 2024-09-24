import os
import subprocess

# Path to the file you want to remove
file_path = 'dummy.log'

# Remove the file
if os.path.exists(file_path):
    os.remove(file_path)
    print(f"{file_path} has been removed.")
else:
    print(f"{file_path} does not exist.")

# Configure Git
subprocess.run(['git', 'config', '--global', 'user.name', 'github-actions[bot]'])
subprocess.run(['git', 'config', '--global', 'user.email', 'github-actions[bot]@users.noreply.github.com'])

# Commit and push the changes
subprocess.run(['git', 'add', '.'])
subprocess.run(['git', 'commit', '-m', 'Remove file.txt'])
subprocess.run(['git', 'push'])
