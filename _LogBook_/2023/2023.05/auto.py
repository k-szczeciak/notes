import os

def list_files_in_current_folder():
    # Get the list of files in the current folder
    files = os.listdir()
    return files

def create_text_file_with_list(file_list):
    with open('file_list.txt', 'w') as f:
        for filename in file_list:
            f.write('- [[' + filename + ']]\n')

if __name__ == "__main__":
    file_list = list_files_in_current_folder()
    create_text_file_with_list(file_list)
    print("File list has been saved to 'file_list.txt'")