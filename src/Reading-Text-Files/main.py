
# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
from pathlib import Path
import os

def read_file_content(filename):

    dir = Path(Path.cwd()/ filename)
    # Check that the file exists
    assert any([dir.is_file(), os.path.isfile(filename)]), 'File does not exist'

    file_content: str

    with open (filename, 'r') as file:
        file_content = file.read()
        print(file_content)

    return file_content

def count_words():

    text = read_file_content("./story.txt")

    text = text.strip('!.,?')
    text_list = text.split()
    
    unique_words = set(text_list)
    unique_word_list = list(unique_words)
    my_dict = {}

    for word in unique_word_list:
        count = 0
        for word2 in text_list:
            if word == word2:   count=count+1
            my_dict[word] = count

    return my_dict


d = count_words()
print(d)