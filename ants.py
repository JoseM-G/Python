#Jose Martinez
#jmarti85@ucsc.edu
#programming assignment 5
#This program prints the lyrics for the song, "The ants go marching".

#The dictionary for the phrases that change for each of the ten verses
phrase = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'suck his thumb', 12:'tie his shoe', 13:'climb a tree', 14:'shut the door', 15:'take a dive', 16:'pick up sticks', 17:'look up to heaven', 18:'shut the gate', 19:'check the time', 20:'say the end'}

def song():
    #prints the ten verses of the song
    for i in range(10):
        #prints the first three lines of each verse
        for j in range(3):
            if j < 2:#the first two lines
                print("The ants go marching "+ phrase[i+1]+ " by "+ phrase[i+1]+ ", hurrah! Hurrah!")
            else:#the third line
                print("The ants go marching "+ phrase[i+1]+ " by "+ phrase[i+1]+ "," )
        #prints the fourth line of each verse
        print("The little one stops to "+ phrase[i+11] + ",")

        #prints the rest of the verse
        print("And they all go marching down... \nIn the ground... \nTo get out... \nOf the rain. \nBoom! Boom! Boom!")

song()
