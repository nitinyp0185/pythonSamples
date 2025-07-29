listOne = [1, 2, 3, 4, 5]
listTwo = [6, 7, 8, 9, 10]
print("List One:", listOne)
print("List Two:", listTwo)

listThree = listOne + listTwo
print("List Three (copy of List One):", listThree)
listThree.append(11)
print("List Three after appending 11:", listThree)
print("List One after List Three modification:", listOne)