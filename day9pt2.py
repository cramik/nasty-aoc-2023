histories=open("day9.txt").read().split('\n')
total=0
for history in histories:
	history=[int(_) for _ in history.split(' ')]
	differences=[]
	differences.append(history)
	while any([_!=0 for _ in differences[-1]]):
		new=[]
		for i in range(1,len(differences[-1])):
			new.append(differences[-1][i]-differences[-1][i-1])
		differences.append(new)
	#add zero to left bottom
	differences[-1]+=[0]
	#Calculate up
	for i in range(1,len(differences)):
		differences[-(i+1)]=[differences[-(i+1)][0]-differences[-i][0]]+differences[-(i+1)]
		print(differences[-(i+1)])
	print(differences[0][0])
	total+=differences[0][0]
print(total)