# my shuffle word game
from random import choice

fh = open("/usr/share/dict/words")
lines = fh.readlines()
words = []
for line in lines:
	words.append(line[:-1])

# now I have a list of words

