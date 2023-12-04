total_pts=0
for line in open("day4.txt"):
	numbers=[_.split() for _ in line.split(': ')[1].split('|')]
	count=0
	for number in numbers[1]: # Cards we have
		if number in numbers[0]: count+=1
	if count>0: total_pts+=(2**(count-1))
	print(total_pts)