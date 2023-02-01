import random
import string
print("Welcome to Password Selector")

adjectives = ['fast', 'slow', 'pink', 'grey']

nouns = ['hen', 'cow', 'goat', 'bird']

adjective = random.choice(adjectives)
noun = random.choice(nouns)

number = random.randrange(0, 100)
special_char = random.choice(string.punctuation)

password = adjective + noun + str(number) + special_char
print("My Password is : %s" % password)