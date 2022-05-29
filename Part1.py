file = open("word_count.txt", "r")
read_data = file.read()
per_word = read_data.split()

print("Total Words:", len(per_word))

from collections import Counter

def count_word(file):
  with open(file) as f:
    return Counter(f.read().split())

print("Frequency of words:",count_word("word_count.txt"))