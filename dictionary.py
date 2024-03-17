import json
from difflib import get_close_matches

# Load dictionary data from JSON file
def load_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Function to get definition of a word
def get_definition(word, data):
    word = word.lower()  # Convert input to lowercase for case-insensitivity
    if word in data:
        return data[word]
    elif word.title() in data:  # Check for proper nouns
        return data[word.title()]
    elif word.upper() in data:  # Check for acronyms
        return data[word.upper()]
    else:
        # Get close matches and suggest if available
        suggestions = get_close_matches(word, data.keys(), n=3, cutoff=0.8)
        if suggestions:
            suggestion_str = ', '.join(suggestions)
            return f"Word not found. Did you mean: {suggestion_str}?"
        else:
            return "Word not found. No suggestions available."

if __name__ == "__main__":
    dictionary_data = load_data("dictionary.json")  # Replace "dictionary.json" with your JSON file path

    while True:
        user_input = input("Enter a word to get its definition (or 'quit' to exit): ")
        if user_input.lower() == 'quit':
            print("Exiting program...")
            break
        else:
            definition = get_definition(user_input, dictionary_data)
            print(definition)
