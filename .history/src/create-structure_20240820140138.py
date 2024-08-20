import os

def create_directory_structure(base_path):
    """
    Creates a directory structure for the Python refresher project.

    Parameters:
    base_path (str): The base path where the directory structure will be created.

    Returns:
    None
    """
    directories = [
        "src",
        "notebooks",
        "notes",
        "exercises/leetcode",
        "exercises/hackerrank",
        "exercises/kaggle",
        "resources"
    ]

    for directory in directories:
        # Create each directory within the base path
        path = os.path.join(base_path, directory)
        try:
            os.makedirs(path, exist_ok=True)
            print(f"Directory created: {path}")
        except Exception as e:
            print(f"Failed to create directory {path}: {e}")

def main():
    """
    Main function to set up the directory structure.
    
    Returns:
    None
    """
    # Define the base path where the directories will be created
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    # Create the directory structure
    create_directory_structure(base_path)

if __name__ == "__main__":
    main()
