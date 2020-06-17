'''This week’s exercise is going to be revisiting an old exercise (see Exercise
5), except require the solution in a different way.

Take two lists, say for example these two:

	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements
that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.

import random
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = random.choices(range(30),k = 15)
a = random.choices(range(30),k = 10)

result = []

result_overlaps = [x for x in a if x in b]

result = [result.append(x) or x for x in result_overlaps if x not in result]

print('List 1:', sorted(a))
print('List 2:', sorted(b))
print('Shared values in list 1 and 2:', sorted(result))
