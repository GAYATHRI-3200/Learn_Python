# Find the maximum repeated character in a string without having O(n^2) complexity

from collections import Counter

def max_repeated_char(s):
    count_char = Counter(s)
    return count_char.most_common(1)[0]

# Example usage
s = "abracadabra"
print(max_repeated_char(s))  # ('a', 5)


#approach 2
def max_repeated_character(s):
    # Count the frequency of each character using dictionary comprehension
    char_freq = {char: s.count(char) for char in set(s)}
    # Find the character with the maximum frequency using max() function
    max_char = max(char_freq, key=char_freq.get)
    return max_char

# Test
s = "abracadabra"
print("Maximum repeated character:", max_repeated_character(s))
