#!/usr/bin/python3

from nltk.corpus import wordnet

# setting setence

out_come=wordnet.synsets("pain")
# printing all data
print(out_come)

# definition 
print(out_come[0].definition())

# examples
print(out_come[0].examples())


