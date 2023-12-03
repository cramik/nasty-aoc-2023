import string
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
bad_chars=string.digits+'.'
for number in number_coords:
	is_a_part=False
	for i in range(number[2],number[3]):
		#TL
		
		try: 
			if schematic[number[1]-1][i-1] not in bad_chars: is_a_part=True
		except: pass
		#Above
		try: 
			if schematic[number[1]-1][i] not in bad_chars: is_a_part=True
		except: pass
		#TR
		try: 
			if schematic[number[1]-1][i+1] not in bad_chars: is_a_part=True
		except: pass
		#Left
		try: 
			if schematic[number[1]][i-1] not in bad_chars: is_a_part=True
		except: pass
		#Right
		try: 
			if schematic[number[1]][i+1] not in bad_chars: is_a_part=True
		except: pass
		#BL
		try: 
			if schematic[number[1]+1][i-1] not in bad_chars: is_a_part=True
		except: pass
		#Below
		try: 
			if schematic[number[1]+1][i] not in bad_chars: is_a_part=True
		except: pass
		#BR
		try: 
			if schematic[number[1]+1][i+1] not in bad_chars: is_a_part=True
		except: pass
	if is_a_part: part_numbers.append(number[0])
part_numbers=[int("".join(_)) for _ in part_numbers]
print(part_numbers)
print(sum(part_numbers))