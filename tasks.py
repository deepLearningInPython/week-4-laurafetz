import numpy as np

# Follow the tasks below to practice basic Python concepts.
# Write your code in between the dashed lines.
# Don't import additional packages. Numpy suffices.

# [A] List Comprehensions and String Manipulation: Tokenization
#     Objective: Practice list comprehensions and basic string operations: split a sentence 
#                into individual words and use list comprehensions to make the code cleaner 
#                and more readable.

# List comprehension provides a concise way to create lists by embedding a for-loop inside 
# square brackets.
# Syntax: [expression for item in iterable if condition] (condition is optional).
# Example: squares = [x**2 for x in range(10) if x % 2 == 0]

# Large language models work with "tokens," which are the basic units of text (often words or subwords). 
# Tokenization is the process of breaking down sentences into these tokens. In this exercise, you’ll 
# create a simple tokenizer to split a sentence into words and remove punctuation.



# Task 1: Given a paragraph of text, implement a simple "tokenizer" that splits the paragraph 
#   into individual words (tokens) and removes any punctuation. Implement this using a list 
#   comprehension.

# Your code here:
# -----------------------------------------------
text = "The quick brown fox jumps over the lazy dog!"

# Write a list comprehension to tokenize the text and remove punctuation
tokens = [word.strip('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~') for word in text.split() if word.strip('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')]

# Expected output: ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
print(tokens)
# -----------------------------------------------




# Task 2: Create a function that takes a string and breaks it up into tokens and removes any 
#   punctuation, and then converts each token to lowercase. The function should returns unique 
#   words in alphabetical order.

# Your code here:
# -----------------------------------------------
def tokenize(string: str) -> list:
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    tokens = {
        word.strip(punctuation).lower()
        for word in string.split()
        if word.strip(punctuation)
    }
    return sorted(tokens)
# -----------------------------------------------



# [B] Dictionary Comprehensions: Frequency Count of Tokens
#     Objective: Practice dictionary comprehensions for token frequency counts.

# Dictionary comprehension is a concise way to create dictionaries using a for-loop inside curly braces.
# Syntax: {key: value for item in iterable if condition} (condition is optional).
# Example: char_count = {char: ord(char) for char in "hello" if char != 'e'}

# Once tokens are extracted, a common task in NLP is to count how often each word appears. 
# This is called calculating the frequency of tokens, and it’s useful because words that appear 
# frequently might have different importance compared to rare words. In this exercise, you’ll 
# create a dictionary where each word is a key and its frequency (count) is the value.



# Task 3: Using the tokens list from the previous exercise, create a dictionary comprehension 
#   that counts the frequency of each word.

# Using the list of tokens from Exercise 1, count the frequency of each word within one 
# dictionary comprehension

# Your code here:
# -----------------------------------------------
word_frequencies = {word: tokens.count(word) for word in set(tokens)}

# Expected output example: {'the': 2, 'quick': 1, ...}
print(word_frequencies)

# Modify the comprehension to include only words that appear more than once.
word_frequencies_2 = {word: tokens.count(word) for word in set(tokens) if tokens.count(word) > 1}
# -----------------------------------------------



# Task 4: Define a function that takes a string and an integer k, and returns a dictionary with
#   the token frequencies of only those tokens that occur more than k times in the string.

    
# Your code here:
# -----------------------------------------------
def token_counts(string: str, k: int = 1) -> dict:
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    tokens = [word.strip(punctuation).lower() for word in string.split() if word.strip(punctuation)]
    token_frequencies = {word: tokens.count(word) for word in set(tokens) if tokens.count(word) > k}
    return token_frequencies

# test:
text_hist = {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}
all(text_hist[key] == value for key, value in token_counts(text).items())
# -----------------------------------------------
