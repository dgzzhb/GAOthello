f = open("input.txt", "r+")
line = f.readline()
f.close()
f = open("output.txt", "w")
line = line[:-2]
seq = (line, ", ", "88", "]")
f.write(''.join(seq))
f.close()