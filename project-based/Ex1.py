from collections import Counter
import string

def word_frequency(text):
    # Remove punctuation and convert to lowercase
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    
    # Split into words and count
    words = text.split()
    word_counts = Counter(words)
    
    # Sort by frequency
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_words

def main():
    # Get input from user
    text = input("Enter your text: ")
    
    # Get and display results
    result = word_frequency(text)
    print("\nWord frequency:")
    for word, count in result:
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()