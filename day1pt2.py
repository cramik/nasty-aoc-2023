import re
digits=['0','1','2','3','4','5','6','7','8','9']
words={"zero":'0',"one":'1',"two":'2',"three":'3',"four":'4',"five":'5',"six":'6',"seven":'7',"eight":'8',"nine":'9'}
total=0
for line in open("day1.txt",'r'):
	print(line)
	numbers=[]
	for digit in digits:
		temps=[m.start() for m in re.finditer(digit,line)]
		for temp in temps: numbers.append((temp,digit))
	for word in words:
		temps=[m.start() for m in re.finditer(word,line)]
		for temp in temps: numbers.append((temp,words[word]))
	numbers.sort(key=lambda tup: tup[0])
	print(numbers)
	if len(numbers)>1: linesol=eval(f"{numbers[0][1]}{numbers[-1][1]}")
	elif len(numbers)==1: linesol=eval(f"{numbers[0][1]}{numbers[0][1]}")
	else: throw("wtf")
	total+=linesol
print(total)