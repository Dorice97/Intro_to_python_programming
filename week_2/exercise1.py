# program that counts number of words in a sentence

def count_words(sentence):
  
    words = sentence.split()
    return len(words)
sentence = input("Enter a sentence: ")
print("Number of words:", count_words(sentence))

def anogram_words():

    def are_anagrams(word1, word2):
        return sorted(word1) == sorted(word2)
    
        print(are_anagrams("stone", "tones")) 

#count number of words in a sentence
line='we want pizza right now'
words=line.split()
print(len(words))



