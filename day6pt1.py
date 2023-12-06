import numpy as np
import re

data=open("day6.txt",'r').read().split('\n')
times=[int(_) for _ in re.findall("\d+",data[0])]
distances=[int(_) for _ in re.findall("\d+",data[1])]
ways=[0]*len(times)

for i in range(len(times)):
	for j in range(times[i]):
		if ((times[i]-j)*j)>distances[i]: ways[i]+=1
	
print(ways)
print(np.prod(ways))