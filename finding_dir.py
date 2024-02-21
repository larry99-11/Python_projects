import os
import re

def search_keyword_in_files(directory, keyword):
    keyword_matches = []

    # Walk through the directory
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            
            # Check if the file is a text file
            if file.endswith('.txt'):
                try:
                    with open(file_path, 'r') as f:
                        # Read the file contents
                        content = f.read()
                        # Search for the keyword using regular expression
                        matches = re.findall(keyword, content)
                        # If keyword found, add to matches list
                        if matches:
                            keyword_matches.append((file_path, matches))
                except Exception as e:
                    print(f"Error reading file {file_path}: {e}")

    return keyword_matches

# Example usage
directory = '/path/to/your/directory'
keyword = 'your_keyword'
matches = search_keyword_in_files(directory, keyword)
for file_path, keyword_occurrences in matches:
    print(f"Keyword '{keyword}' found in file '{file_path}': {len(keyword_occurrences)} occurrences")
