import os

def list_files_in_current_folder(exclude_extensions=[]):
    files = os.listdir()
    filtered_files = [file for file in files if not any(file.endswith(ext) for ext in exclude_extensions)]
    return filtered_files

def create_text_file_with_list(file_list):
    with open('file_list.txt', 'w') as f:
        for filename in file_list:
            
            f.write('- [[' + filename + ']]\n')

if __name__ == "__main__":
    excluded_extensions = ['.py']
    file_list = list_files_in_current_folder(excluded_extensions)
    create_text_file_with_list(file_list)
    print("File list (excluding Python files) has been saved to 'file_list.txt'")