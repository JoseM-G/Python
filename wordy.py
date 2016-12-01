#Jose Martinez
#jmarti85@ucsc.edu
#programming assignment 3
#This program takes in a user input sentence and calculates the average word length and word count of the sentence. This program also ignores the following punctuation: ",", ",", "!", "?".

def analyze():
    #The initial user input sentence
    sentence = input("Please write a sentence. ")
    #The user input sentence stripped of unwanted punctuation
    modified = sentence.replace(".", "").replace(",", "").replace("!", "").replace("?", "")
    #It is then taken and stripped of excess spaces
    again = modified.strip(" ")
    #The reamining number of spaces in the sentence are counted
    spaces = again.count(" ")
    #One is added to this count and that is the word count of the sentence
    words = spaces + 1
    #Word count is printed
    print ("Your sentence has", words,"words")
    
    count = 0
    #This for loop goes through the string and counts the characters that aren't spaces
    for i in range(len(again)):
        if modified[i] != " ":
            count = count +1

    #That number is then divided by the word count to find the average word length
    average = count / words
    #Average word length is printed
    print("The average word length of your sentence is approximately", round(average, 2))

analyze()
