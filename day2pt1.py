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
		
		if counts["red"]>12 or counts["green"]>13 or counts["blue"]>14:
			possible=False
		if game[3+i*2].find(';')!=-1: counts_max={"blue": max((counts_max['blue'],counts['blue']), "red":max((counts_max['red'],counts['red']),"green":max((counts_max['red'],counts['red'])}
	if possible: total+=int(game_id)
print(total)