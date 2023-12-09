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
	prediction=sum([difference[-1] for difference in differences])
	total+=prediction
print(total)