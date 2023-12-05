from concurrent.futures import ProcessPoolExecutor
from numba import jit, prange
import re
import numpy as np

# WARNING -- THIS CODE TAKES PREPROCESSING OF YOUR INPUT.
# BECAUSE IT USES NUMBA YOU NEED TO MAKE ALL OF YOUR MAPS THE
# SAME SIZE (BY ADDING DUPLICATE ENTRIES) IN ORDER TO FIT IN
# A NUMPY ARRAY :P
# THIS IS PROBABLY A TERRIBLE SOLUTION BUT A) IT'S FUNNY B) IT WORKS


data=open("day5.txt").read()
seed_ranges_text=re.findall("seeds: (.+?)\n\n",data)[0]
seed_ranges=[_.split() for _ in re.findall("\d+ \d+",seed_ranges_text)]
new_seed_ranges=[]
for seed_range in seed_ranges:
	new_seed_ranges.append([int(_) for _ in seed_range])
new_seed_ranges=np.array(new_seed_ranges)



def map_helper(text):
	if text=="humidity-to-location": map=[_.split() for _ in re.findall(f"{text} map:\n(.+)",data,flags=re.DOTALL)[0].split('\n')]
	else: map=[_.split() for _ in re.findall(f"{text} map:\n(.+?)\n\n",data,flags=re.DOTALL)[0].split('\n')]
	return map

maps=[map_helper("seed-to-soil"),map_helper("soil-to-fertilizer"),map_helper("fertilizer-to-water"),map_helper("water-to-light"),map_helper("light-to-temperature"),map_helper("temperature-to-humidity"),map_helper("humidity-to-location")]
newmaps=[]
for map in maps:
	newmap=[]
	for item in map:
		newmap.append([int(_) for _ in item])
	newmaps.append(newmap)
newmaps=np.array(newmaps)

@jit(nopython=True)
def range_helper(seed_range):
	min_location=100000000000000
	for i in prange(seed_range[1]):
		current=seed_range[0]+i
		for map in newmaps:
			for item in map:
				if (current-item[1])>=0:
					if (current-item[1])<item[2]: 
						current = item[0]+(current-item[1])
						break
		if current<min_location: 
			min_location=current
	print(min_location)
	return min_location

#Navigate map
if __name__ == '__main__':
	
	with ProcessPoolExecutor(max_workers=20) as exe:
		results=exe.map(range_helper,new_seed_ranges)

	print(min(results))