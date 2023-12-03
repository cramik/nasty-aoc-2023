import string
import numpy as np

lines = open("day3.txt",'r').read().split()
schematic=[]
for line in lines:
	schematic.append([_ for _ in line])
number_coords=[]
for i in range(len(schematic)):
	on_a_number=False
	for j in range(len(line)):
		if schematic[i][j].isdigit(): 
			if not on_a_number: 
				on_a_number=True
				start_index=j
		else:
			if on_a_number:
				end_index=j
				number_coords.append((schematic[i][start_index:end_index],i,start_index,end_index))
				on_a_number=False
	if on_a_number:
		end_index=j+1
		number_coords.append((schematic[i][start_index:end_index],i,start_index,end_index))
print(number_coords)

part_numbers=[]
gear_parts=[]
bad_chars=string.digits+'.'
for number in number_coords:
	gears=[]
	for i in range(number[2],number[3]):
		#TL
		
		try: 
			if schematic[number[1]-1][i-1]=='*': 
				if (number[1]-1,i-1) not in gears: gears.append((number[1]-1,i-1))
		except: pass
		#Above
		try: 
			if schematic[number[1]-1][i]=='*': 
				if (number[1]-1,i) not in gears: gears.append((number[1]-1,i))
		except: pass
		#TR
		try: 
			if schematic[number[1]-1][i+1]=='*': 
				if (number[1]-1,i+1) not in gears: gears.append((number[1]-1,i+1))
		except: pass
		#Left
		try: 
			if schematic[number[1]][i-1]=='*': 
				if (number[1],i-1) not in gears: gears.append((number[1],i-1))
		except: pass
		#Right
		try: 
			if schematic[number[1]][i+1]=='*': 
				if (number[1],i+1) not in gears: gears.append((number[1],i+1))
		except: pass
		#BL
		try: 
			if schematic[number[1]+1][i-1]=='*': 
				if (number[1]+1,i-1) not in gears: gears.append((number[1]+1,i-1))
		except: pass
		#Below
		try: 
			if schematic[number[1]+1][i]=='*': 
					if (number[1]+1,i) not in gears: gears.append((number[1]+1,i))
		except: pass
		#BR
		try: 
			if schematic[number[1]+1][i+1]=='*': 
					if (number[1]+1,i+1) not in gears: gears.append((number[1]+1,i+1))
		except: pass
	if len(gears)>0: gear_parts.append((int("".join(number[0])),gears))
print(gear_parts)
#Doing this dict part after is smart if we get duplicate numbers, rare edge case but good excuse
gear_dict={}
for gear_part in gear_parts:
	if gear_dict.get(str(gear_part[1])) is not None: gear_dict[str(gear_part[1])].append(gear_part[0])
	else: gear_dict[str(gear_part[1])]=[gear_part[0]]
print(gear_dict)

total=0
for gear in gear_dict:
	if len(gear_dict[gear])>1: #Why is this a requirement?
		total+=np.prod(gear_dict[gear])
print(total)