#Jose Martinez
#jmarti85@ucsc.edu
#programming assignment 6
#This program takes in a user input scrambled word and unscrambles it. It does so by creating a list of all possible permutations of the given word and refences it against a dictionary to confirm any words their jumbled input could make. Note, after inporting you need to write a directory to a dictionary type txt file of your choosing with the following prompt, jumble.main("(Directory here)").

#The main function
def main(dictionary):
    #This block opens the given txt file, opens it, puts it in a readable state and splits it up into a list
    text = open(dictionary, 'r')
    readable = text.read()
    lowercase = readable.lower()
    final = lowercase.split()
    
    number = 0 #Used to count the number of words found within the jumbled input
    correct = {}#Dictionary used to store all the words found within jumbled input

#Asks user for a jumbled word, makes it all characters lower case and plugs into function that generates permutations 
    jumbled_word = input("Please enter a jumbled word: ")
    modified_word = jumbled_word.lower()
    jumble(modified_word)

#Goes through list of permutations and compares them to the dictionary provided by the user and puts the actual words into the "correct" dictionary
    for j in jumble(modified_word):
        if j in final:
            correct[number] = j
            number = number +1

#Prints this if only one word can be made with jumbled input, 
    if number == 1: 
        print("Your word is "+correct[0]+".")
#Prints this if more than one word can be made from jumbled input
    if number > 1:
        print("Your words are:")
        for k in correct:
            print(correct[k])
#Prints this no words can be formed from jumbled input
    elif number == 0:
         print("Your word cannot be unjumbled.")

#Function that generates all permutations of the given jumbled word, based off of anagram examples provided on the course website 
def jumble(word):
    if word  == "":
        return([""])
    else:
        first = word[0]
        remainder = word[1:]
        small_list = jumble(remainder)
        full_list = []
        for partial in small_list:
            for i in range(len(partial)+1):
                new_word = partial[:i] + first + partial[i:]
                full_list = full_list + [new_word]
                
    full_list = list(set(full_list)) #removes duplicates
    return(full_list)


