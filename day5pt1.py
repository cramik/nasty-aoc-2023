import re

data=open("day5sample.txt").read()
seeds=re.findall("seeds: (.+?)\n\n",data)[0].split()
print(seeds)

def map_helper(text):
	if text=="humidity-to-location": map=[_.split() for _ in re.findall(f"{text} map:\n(.+)",data,flags=re.DOTALL)[0].split('\n')]
	else: map=[_.split() for _ in re.findall(f"{text} map:\n(.+?)\n\n",data,flags=re.DOTALL)[0].split('\n')]
	return map

maps=[map_helper("seed-to-soil"),map_helper("soil-to-fertilizer"),map_helper("fertilizer-to-water"),map_helper("water-to-light"),map_helper("light-to-temperature"),map_helper("temperature-to-humidity"),map_helper("humidity-to-location")]


#Navigate map
locations=[]
for seed in seeds:
	current=int(seed)
	for map in maps:
		for item in map:
			item=[int(_) for _ in item]
			if (current-item[1])>0:
				if (current-item[1])<item[2]: 
					current = item[0]+(current-item[1])
					break
	locations.append(current)

print(locations)
print(min(locations))