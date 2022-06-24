'''
Takes 2 strings, return a bool
Check if the two strings are anagrams: same character are present in the same amount in both strings
'''

def is_anagram(word1, word2):
    if len(word1) != len(word2):
        return False
    freq1 = {}
    freq2 = {}
    for i in range(len(word1)):
        # record frequency of letter in both words in seperate dicts
        freq_add(word1[i], freq1)
        freq_add(word2[i], freq2)
    if freq1 == freq2:
        return True
    else:
        return False

def freq_add(letter, freq):
    ''' adds letter to a frequency dict'''
    if letter in freq:
        freq[letter] += 1
    else:
        freq[letter] = 1

