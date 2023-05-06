import os
import sys

def count_words(filename, word_counts=None):
    if not word_counts:
        word_counts = {}
    if not os.path.isfile(filename):
        print(f"Error: {filename} does not exist or is not a file.")
        return word_counts
    with open(filename, 'r') as file:
        line = file.readline().strip()
        if not line:
            return word_counts
        words = line.split()
        for word in words:
            if word not in word_counts:
                word_counts[word] = 1
            else:
                word_counts[word] += 1
        return count_words(filename, word_counts)

sys.setrecursionlimit(1000)
filename = input("Enter the file name: ")
word_counts = count_words(filename)
print(word_counts)
