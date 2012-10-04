timbits = int(input())

largeBoxes = int(timbits / 40)
rest = timbits - largeBoxes * 40
totalCost = largeBoxes * 6.19

mediumBoxes = int(rest / 20)
rest = rest - mediumBoxes * 20
totalCost = totalCost + mediumBoxes * 3.39

smallBoxes = int(rest / 10)
rest = rest - smallBoxes * 10
totalCost = totalCost + smallBoxes * 1.99

separateTimbits = rest
totalCost = totalCost + separateTimbits * 0.20

print('the number of large boxes is:', largeBoxes)
print('the number of medium boxes is:', mediumBoxes)
print('the number of small boxes is:', smallBoxes)
print('the number of separate timbits is:', separateTimbits)
print('the total cost is:', totalCost)

