cards=open("day4.txt").read().split('\n')
card_count={}
for i in range(len(cards)):
	card_count[i]=1

for i in range(len(cards)):
	numbers=[_.split() for _ in cards[i].split(': ')[1].split('|')]
	count=0
	for number in numbers[1]: # Cards we have
		if number in numbers[0]: count+=1
	if count>0:
		for j in range(i+1,i+count+1): 
			card_count[j]+=card_count[i]
	

print(card_count)
total=0
for i in range(len(cards)):
	total+=card_count[i]
print(total)