#Jose Martinez
#jmarti85@ucsc.edu
#programming assignment 1
#This program will generate a random integer from 1 to 10 and gives the user 3 attempts to guess. The user will also be given hints, like if the number is too big or too small to narrow down the possibilities

def game():
      print("I'm thinking of an integer, you have three guesses.")
      import random
      rand_integer = random.randint(1, 10)
      for i in range(3):
          user_integer = eval(input("Guess "+str(i+1)+": Please enter an integer between 1 and 10: "))
          if user_integer > rand_integer:
              if i == 2:
                  print("Too bad. The number is:", rand_integer)
                  break
              else:
                  print("Your guess is too big")
          if user_integer < rand_integer:
              if i == 2:
                  print("Too bad. The number is:", rand_integer)
                  break
              else:
                  print("Your guess is too small")
          if user_integer == rand_integer:
              print("You got it!")
              break

game()
                  
