# Madlibs Test

import random

def ML():
    a = input("Would you like to play madlibs? (y/n): ")
    if a == "y":
      def madlibs():
         verb1 = input("Choose a verb: ")
         verb2 = input("Choose a verb: ")
         noun = input("Choose a noun: ")
         adj = input("Choose an adjective: ")

         sentence1 = f"I will {verb1} with my friends, then i'll {verb2} to my {adj} {noun}"
         sentence2 = f"I want to get {verb1} with my friends, then I will {verb2} my {adj} {noun}"
         b = [sentence1, sentence2];
         print(random.choice(b));
         c = input("That was so fun! Would you like to play again?: ");
         if c == "yes":
            ML();
         else:
            print("Okay then, have a nice day!");
      madlibs();
    elif a == "Y":
      def madlibs():
         verb1 = input("Choose a verb: ")
         verb2 = input("Choose a verb: ")
         noun = input("Choose a noun: ")
         adj = input("Choose an adjective: ")

         sentence1 = f"I will {verb1} with my friends, then i'll {verb2} to my {adj} {noun}"
         sentence2 = f"I want to get {verb1} with my friends, then I will {verb2} my {adj} {noun}"
         b = [sentence1, sentence2];
         print(random.choice(b));
         c = input("That was so fun! Would you like to play again?: ");
         if c == "yes":
            ML();
         else:
            print("Okay then, have a nice day!");
      madlibs();
    elif a == "n":
      print("Okay then, have a nice day!");
    elif a == "N":
      print("Okay then, have a nice day!");
    else:
       print("Invalid Input")
ML();