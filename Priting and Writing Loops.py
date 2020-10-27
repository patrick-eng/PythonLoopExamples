#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 12:18:49 2020

@author: patrickenglish

This script starts with some basic stuff on loops in Python.

Then, it makes a fun exchange of questions and suggestions between two
imaginary characters - Mark and Harriet. 

What will they do with all their stuff?!

We can write some loops to print out a conversation between the pair of them
into the console, and then use the same code to create a text file where we store
the outcomes.

"""


print("\n-------")

# 1. Some basic loop examples 

# Make a short list of numbers
numbers = [1, 2, 3, 4, 5]

# loop to print them
for z in numbers:
    print(z)
# the numbers 1 to 5 are printed

print("\n-------")

# Now, print out the element number (rather than the number itself)
for x in range(5):
    print(x)
# Note 1: now we are working with elements, the numbers 0 to 4 are printed instead.
# The loop starts at position 0, and ends before printing the limit of the range (5)    

print("\n-------")

# Make a short list of words
y = ["Cats", "Dogs", "Rabbits", "Sparrows"]    

# Print out each unique word
for i in y:
    print(i)

print("\n-------")


# Now we are going to use loops to write a little story!

# 3. Import the random package
import random


# 4. Define our list of words and options
words = ["boats", "dollar bills", "buildings", "cars", "planes", "shot glasses"]

options = ["burn them with fire", "eat them", "do a rain dance, maybe they'll go away",
           "take them all", "shoot them with the submarine",
           "send them to the moon"]


# 5. Set up the loop to print out the conversation to the console/window. Also, let's leave
# a little note for ourselves which tells us which random response for Harriet was picked.
for i in words:
    selection = random.choice(options)
    print("Mark: What shall we do with all the", i + "?")
    print("Harriet: We should", selection + ".")
    position = options.index(selection)
    print("(By the way, the selection was element number", position, "in the options list)")
    print("  ")
    
# Note 1: Using + means no space in between printed objects, but a comma means a space 
# Note 2: Don't forget that python elements start at 0
   
    
# 6. Set up the loop to write the conversation to a text file. Remember we need to define 
# that we are writing to the file using the "w" option.    
file = open("WhatShallWeDo.txt", "w")    

for i in words:
    selection = random.choice(options)
    position = options.index(selection)
    file.write("Mark: What shall we do with all the " + i + "?\n")
    file.write("Harriet: " + selection + "\n")
    file.write("(By the way, the selection was element " + str(position) + " in the options list) \n")
    file.write("-----\n")

file.close()