import re

data=open("day6.txt",'r').read().split('\n')
time=int(''.join([_ for _ in re.findall("\d+",data[0])]))
distance=int(''.join([_ for _ in re.findall("\d+",data[1])]))
ways=0

for j in range(time):
	if ((time-j)*j)>distance: ways+=1
	
print(ways)