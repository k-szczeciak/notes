import os

def find_common_prefix(strings):
    if not strings:
        return ""

    prefix = strings[0]
    for string in strings[1:]:
        while string[:len(prefix)] != prefix and len(prefix) > 0:
            prefix = prefix[:-1]
        if not prefix:
            break
    return prefix

def list_files_in_current_folder(exclude_extensions=[]):
    files = os.listdir()
    filtered_files = [file for file in files if any(file.endswith(ext) for ext in exclude_extensions)]
    return filtered_files

def create_text_file_with_list(file_list, common_prefix):
    file_name = common_prefix if common_prefix else "no_common_prefix"
    with open(f'{file_name}log.md', 'w') as f:
        for filename in file_list:
            f.write('- [[' + filename + ']]\n')
        f.write(f"Number of days: {len(file_list)}\n")

if __name__ == "__main__":
    excluded_extensions = ['.md']
    file_list = list_files_in_current_folder(excluded_extensions)
    common_prefix = find_common_prefix(file_list)
    create_text_file_with_list(file_list, common_prefix)
    print(f"File list (excluding Python files) has been saved to '{common_prefix}_file_list.txt'")
