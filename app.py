import json
import difflib

def load_dictionary(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def get_definition(word, dictionary):
    # Normalize the word to lower case
    word = word.lower()
    
    # Check if the word exists in the dictionary
    if word in dictionary:
        return dictionary[word]
    else:
        # Suggest a close match if the word is not found
        suggestions = difflib.get_close_matches(word, dictionary.keys())
        if suggestions:
            return f"'{word}' not found. Did you mean: {', '.join(suggestions)}?"
        else:
            return f"'{word}' not found and no suggestions available."
        
def main():
    # Load the dictionary from a JSON file
    dictionary = load_dictionary('dictionary_data.json')
    
    # Get user input
    user_input = input("Enter a word: ")
    
    # Get the definition or suggestion
    result = get_definition(user_input, dictionary)
    
    print(result)

if __name__ == "__main__":
    main()