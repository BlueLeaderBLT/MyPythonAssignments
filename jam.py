# my Code Jam Problem

fh = open("data.in")
lines = fh.readlines()
phrases = []
for line in lines[1:]:
	if line[-1] == '\n':
		line = line[:-1]
	phrases.append(line)



