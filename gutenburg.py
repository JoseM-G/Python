#CMPS5P
#May 6, 2015
#This program opens a downloaded book from the computer (saved as a text file), then counts the number of words, after removing punctuation. Finally we print the average number of characters per word.

import string


def word_count_squared(book):
    number_of_words = word_stats(book)
    number_squared = number_of_words **2
    print(number_squared)
    

def word_stats(book):
    opened_book = open(book,'r')
    long_string = opened_book.read()
    no_newline = long_string.replace("\n"," ")
    for x in string.punctuation:
        no_newline = no_newline.replace(x,"")
    list_of_words = no_newline.split(" ")
    word_count = len(list_of_words)
    print("The word count is ",word_count)
    clean_string = no_newline.replace(" ","")
    total_char = len(clean_string)
    print("The average word length is ",total_char/word_count)
    #now the function will return the word count
    return(word_count)
    
    

