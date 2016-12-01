# June 3, 2015
# CMPS5P
# This python program takes a string as a parameter and returns a list of all possible permutations of the string. This python program uses recursion.

def permute(orig):
    #base case
    if orig == "":
        return([""])
    #recursive step
    else:
        first_char = orig[0]
        remainder = orig[1:]
        # small_list will be a list containing all permutations of the the string remainder
        small_list = permute(remainder)
        full_list = []
        for partial_word in small_list:
            #iterate over all possible positions in partial_word
            for i in range(len(partial_word)+1):
                new_word = partial_word[:i] + first_char + partial_word[i:]
                full_list = full_list + [new_word]
        return(full_list)
        
