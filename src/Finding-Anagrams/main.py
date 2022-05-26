# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True



def find_anagram(word: str, anagram: str )-> bool:

    if not (set(anagram.casefold()) == set(word.casefold())):
        return False
  
    return True