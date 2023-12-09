import re

#Preprocess
data=open("day8.txt",'r').read().split('\n\n')
instructions=data[0]
maps={}
for line in data[1].split('\n'):
	map_data=line.split(" = ")
	maps[map_data[0]]=[]
	for path in re.findall("[A-Z]+",map_data[1]): 
		maps[map_data[0]].append(path)


#Count
current="AAA"
instruction_map={"L":0,"R":1}
i=0
while True:
	current=maps[current][instruction_map[instructions[i%len(instructions)]]]
	i+=1
	print(f"{current} {i}")
	if current=="ZZZ": break
print(i)