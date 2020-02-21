def permutations(n):
	if n == 1:
		return [[1]]

	p = permutations(n-1)

	ans = []
	for x in p:
		for i in range(n):
			new_x = x[:i] + [n] + x[i:]
			ans.append(new_x)

	return ans

def valid(i1, j1, i2, j2):
	return i1 != i2 and j1!= j2 and abs(i1-i2) != abs(j1-j2)

size = 8
perm8 = permutations(size)

number = 0
for x in perm8:
	flag = True
	for i in range(size):
		for j in range(i+1, size):
			if not valid(i, x[i], j, x[j]):
				flag = False

	if flag:
		number += 1

print("The number of solutions is: {}.".format(number))
