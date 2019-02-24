import stemmer

def findWords(target, text):
	list1 = []
	counter = 0
	count = 0
	for line in text:
		for word in line.split():
			counter += 1
			if word == target:
				count += 1
				list1.append(counter)
	list1.append(count)
	return list1
	

target1 = 'happiness'
target2 = 'promise'
text = open("emma.txt", "r")




list2 = findWords(target1, text)
list3 = findWords(target2, text)

count1 = list2[len(list2)-1]
count2 = list3[len(list3)-1]

print (count1)
print(list2)

print(list3)
