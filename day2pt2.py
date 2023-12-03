total=0
for line in open("day2.txt",'r'):
	game=line.split()
	counts={"blue": 0, "red":0,"green":0}
	counts_max={"blue": 0, "red":0,"green":0}
	game_id=game[1].replace(':','')
	print(game)
	pulls=int((len(game)-2)/2)
	possible=True
	for i in range(pulls):
		counts[game[3+i*2].replace(',','').replace(';','')]+=int(game[2+i*2])
		if game[3+i*2].find(';')!=-1: 
			counts_max={"blue": max((counts_max['blue'],counts['blue'])), "red":max((counts_max['red'],counts['red'])),"green":max((counts_max['green'],counts['green']))}
			counts={"blue": 0, "red":0,"green":0}
	counts_max={"blue": max((counts_max['blue'],counts['blue'])), "red":max((counts_max['red'],counts['red'])),"green":max((counts_max['green'],counts['green']))}
	print(counts_max)
	power=counts_max['blue']*counts_max['red']*counts_max['green']
	total+=power
print(total)