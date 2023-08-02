def anagrams(word1, word2):
    word1 = sorted(word1)
    word2 = sorted(word2)
    i = 0
    anagram = ''
    if len(word1) != len(word2):
        anagram = 'no'
    else:
        while i < len(word1) and i < len(word2):
            if word1[i] == word2[i]:
                anagram = 'yes'
            elif word1[i] != word2[i]:
                anagram = 'no'
                break
            i += 1
    if anagram == 'yes':
        return True
    return False

if __name__ == "__main__":
    print(anagrams("test", "sett"))