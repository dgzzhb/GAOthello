from random import randint

f = open('firstGeneration', 'w')

for i in xrange(20):
	board = []
	for j in xrange(16):
		seed = randint(-100,100)
		board.append(seed)
	f.write(str(board))
	f.write('\n')
    
f.close()