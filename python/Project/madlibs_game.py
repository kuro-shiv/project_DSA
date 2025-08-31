# madlibs_game.py
# This program is an extended Mad Libs game where the user inputs words to create a funny story

# Taking inputs from the user
name = input("Enter a name: ")
place = input("Enter a place: ")
adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
plural_noun = input("Enter a plural noun: ")
exclamation = input("Enter an exclamation: ")
animal = input("Enter an animal: ")
food = input("Enter a food: ")
color = input("Enter a color: ")
profession = input("Enter a profession: ")
hobby = input("Enter a hobby: ")

# Creating the extended story using user inputs
story = f"""
Once upon a time, {name} went to {place}. 
It was a very {adjective} day and the sun was shining brightly. 
Suddenly, a {noun} appeared and started to {verb} right in front of everyone! 
All the {plural_noun} shouted, "{exclamation}!" 
Then, a {color} {animal} ran by carrying a {food}. 
A {profession} nearby was so surprised that they dropped their {hobby} on the ground. 
{name} realized that life in {place} was always full of surprises and laughter. 
Everyone joined in to help {name} and the day turned into an unforgettable adventure. 
By the end of the day, {name} promised to always keep an eye out for the unexpected.
"""

# Printing the final Mad Libs story
print(story)
