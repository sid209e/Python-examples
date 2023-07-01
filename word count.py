"""Create a Python program that reads a text file and counts the
occurrences of each word. You can use a dictionary to store the
words as keys and their counts as values."""

def count_words(filename):
    word_counts = {}

    with open(filename, "r") as file:
        for line in file:
            words = line.strip().split()
            print(words)
            for word in words:
                word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts


filename ="sample.txt"
word_counts = count_words(filename)
for word, count in word_counts.items():
    print(f"{word}:{count}")