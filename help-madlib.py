
# Homework: Create a madlib. Imagine a story where some of the words are 
# supplied by user input. Using python you will use input to collect 
# words for a story and then display the story. 

# Use input to collect each word to a variable
# Use an f string to display the story

# Your madlib must collect at least 6 words!

print('\n"Helping a Friend Mad Lib"\n')
favorite_toy = input("Please enter Your Favorite Toy: ")
silly_name = input("Please enter a Silly Name: ")
boys_name = input("Please enter a Boy's Name: ")
favorite_beverage = input("Please enter Your Favorite Beverage: ")
object = input("Please enter an Object's Name: ")
emotion = input("Please enter an Emotion: ")
another_emotion = input("Please enter One More Emotion: ")
adjective = input("Please enter an Adjective: ")
another_adjective = input("Please enter One More Adjective: ")
animal = input("Please enter an Animal: ")

print(f"\nOnce upon a time, there was a {favorite_toy} named {silly_name}. {silly_name} was a very good {favorite_toy} and it made everyone very happy.\nOne day {silly_name} ran out of {favorite_beverage}, it needed {favorite_beverage} to move, you see!\n{silly_name} could not move. {silly_name} got very {emotion} but then its friend {boys_name} came.\n{boys_name} wanted to fill {silly_name}'s tank with {favorite_beverage} but he did not know how to fill {silly_name}'s tank, so he watched a video on how to fill {silly_name}'s tank with {favorite_beverage}.\n{boys_name} was very {adjective} and he was able to fill {silly_name}'s tank after watching the video on his {object}.\n{silly_name} said, Thanks {boys_name}! You are my {another_adjective} {animal}.\n")

# This story is written by (told by) my 4 year old son, Ivan. He loved playing with this MadLib and providing the inputs over and over again. 
# I had to explain the meaning of adjectives and objects to him but after that he didn't stop for next 30-35 minutes. :) 