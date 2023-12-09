def replacer(val):
	dictionary={'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'A':14}
	return_val=[]
	for letter in val:
		return_val.append(dictionary[letter])
	return(return_val)

plays=[_.split(" ") for _ in open("day7.txt",'r').read().split('\n')]
plays=[[replacer(play[0])]+[int(play[1])] for play in plays]


reverse_cards=['2','3','4','5','6','7','8','9','T','J','Q','K','A']
# 0 = high, 1=one, 2=two, 3=three, 4= house, 5=four, 6=five
definitions={0:[],1:[],2:[],3:[],4:[],5:[],6:[]}
for play in plays:
	hand=play[0]
	definition=0
	for card in set(hand):
		if hand.count(card)==2:
			for other_card in set(hand):
				if hand.count(other_card)==2 and card!=other_card:
					definition=max(definition,2)
			definition=max(definition,1)
		if hand.count(card)==3: 
			for other_card in set(hand):
				if hand.count(other_card)==2: 
					definition=max(definition,4)
			definition=max(definition,3)
		if hand.count(card)==4: 
			definition=max(definition,5)
		if hand.count(card)==5: 
			definition=max(definition,6)
		else:
			definition=max(definition,0)
	definitions[definition].append(play)

rank=1
total=0

for definition in definitions:
	definitions[definition].sort(key=lambda tup: tup[0])
	for play in definitions[definition]:
		total+=rank*play[1]
		rank+=1
print(total)