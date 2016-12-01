#Jose Martinez
#jmarti85@ucsc.edu
#programming assignment 4
#This program reads a text file and composes a dictionary that shows how many times a word appears in the text. To look up a word first you need to open a text file by typing text = shakespeare.dictionary("(directory of text file)"). Then to look up the count of a specific word type text['(word)'].

#Used for alternate method to remove punctuation
import string

def dictionary(book):
    #the text is set to a readable format and reads the file
    text = open(book, 'r')
    open_book = text.read()
    
    #changes any capitalized letters into a lower case so the count for a word isn't affected by difference in lower case and upper case.
    book_lower = open_book.lower()

    #alternate method to remove punctuation
    #remove_punct = {ord(c): None for c in string.punctuation}
    #no_punctuation = book_lower.translate(remove_punct)

    #method to remove punctuation used in the gutenberg.py example
    for x in string.punctuation:
        book_lower = book_lower.replace(x,"")

    #for some reason setting the string with the removed punctuation to a new variable produces undesired results. For example if looking up text['laugh'] it says it occurs 3 times instead of 6 but it works just fine for text['the'] showing it occurs 993 times.
    #for x in string.punctuation:
        #no_punctuation = book_lower.replace(x,"") 

    #splits up the text file into a list of the words it is comprised of 
    book_list = book_lower.split()

    #used with the error producing method to remove punctuation
    #book_list = no_punctuation.split()

    #creates the dictionary for the text file
    book_dict = {}

    #goes through the list of words and detects if that word is already in the dictionary or not. If it isn't, it is added and a value of 1 is assigned to it. If it is in the dictionary, its assigned value is increased by 1.
    for i in book_list:
        if not(i in book_dict):
            book_dict[i] = 1
        else:
            book_dict[i] = book_dict[i] + 1

    #returns the dictionary for the function dictionary(book)
    return(book_dict)


